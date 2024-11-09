from dataclasses import dataclass
import json
import os
from typing import Any, Iterator, Optional, Type, TypeVar, Union
import requests

from hevy_api_client.models import (
    ExerciseTemplate,
    ExerciseTemplateGetResponse,
    Model,
    ResponseModel,
    Routine,
    RoutineFolder,
    RoutineFoldersGetResponse,
    RoutineGetResponse,
    Workout,
    WorkoutGetResponse
)
from hevy_api_client.utils import are_dicts_equal

HEVY_API_URL = "https://api.hevyapp.com/v1/"

T = TypeVar("T", bound=Model)


class HevyAPIException(Exception):
    pass


@dataclass()
class APIHandler:
    endpoint: str
    document_id_field: str
    document_create_field: str
    response_model: Type[ResponseModel]
    model: Type[Model]

    _url: str = os.getenv("HEVY_API_URL", HEVY_API_URL)
    _api_key: str = os.getenv("HEVY_API_TOKEN", "")
    page_size: int = 10
    _session = requests.Session()

    def __post_init__(self) -> None:
        if not self._api_key:
            raise ValueError("HEVY_API_TOKEN cannot be missing.")

        self._session.hooks = {
            "response": lambda r, *args, **kwargs: r.raise_for_status()
        }
        self._session.headers = {
            "api-key": self._api_key,
            "accept": "application/json",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        endpoint: Optional[str] = None,
        data: Optional[Union[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:

        if endpoint is None:
            endpoint = self.endpoint

        if data is None:
            data = {}

        return self._session.request(
            method=method,
            url=self._url + endpoint,
            data=json.dumps(data),
        ).json()

    def each(self) -> Iterator[Model]:
        req_params = {
            "method": "GET",
            "data": {
                "page": 0,
                "pageSize": self.page_size
            }
        }

        res = None
        while res is None or res.page_count > res.page:
            req_params["data"]["page"] += 1
            res = self.response_model.model_validate(self._request(**req_params))

            for routine_folder in res.get_fields():
                yield routine_folder

    def get(self, doc_id: int) -> Model:
        req_params = {
            "method": "GET",
            "data": {self.document_id_field: doc_id},
        }
        return self.response_model.model_validate(self._request(**req_params)).get_fields()[0]

    def _find_newly_created_doc(self, res: dict[str, Any], doc: T) -> T:
        """
        There is an error in the API for some docs on create operations where the API
        does not return the newly created doc.

        This method is thought to be a temporary patch to find the newly created doc,
        and is not bulletproof. If 2 exercises share the same properties this function will
        raise an Exception signaling that we were not able to find the newly created doc.
        """

        if res:
            return self.model.model_validate(res)

        new_doc_dict = doc.model_dump(exclude_none=True)

        newly_created_doc_dict: Optional[dict[str, Any]] = next((
            api_doc
            for api_doc in self.each()
            if are_dicts_equal(new_doc_dict, api_doc.model_dump(exclude_none=True))
        ), None)

        if newly_created_doc_dict is None:
            raise HevyAPIException(f"Cannot find newly created {self.model.__name__}: {new_doc_dict}")

        return self.model.model_validate(newly_created_doc_dict)

    def create(self, doc: T) -> T:
        req_params = {
            "method": "POST",
            "data": {self.document_create_field: doc.model_dump(exclude_none=True)},
        }

        res = self._request(**req_params)[self.document_create_field]
        return self._find_newly_created_doc(res, doc)

    def delete(self, doc_id: str):
        raise NotImplementedError("This endpoint is not exposed in the public API yet")


class WorkoutsAPIHandler(APIHandler):
    @property
    def count(self) -> int:
        req_params = {
            "method": "GET",
            "endpoint": "workouts/count"
        }
        return self._request(**req_params)["workout_count"]


class RoutinesAPIHandler(APIHandler):
    def update(self, updated_routine: Routine) -> Routine:
        req_params = {
            "method": "PUT",
            "endpoint": f"routines/{updated_routine.id}",
            "data": updated_routine,
        }
        return Routine.model_validate(self._request(**req_params))


class HevyAPIClient:
    """
    Hevy API Client
    """

    workouts = WorkoutsAPIHandler(
        endpoint="workouts",
        document_id_field="workoutId",
        document_create_field="workout",
        response_model=WorkoutGetResponse,
        model=Workout,
    )
    exercise_templates = APIHandler(
        endpoint="exercise_templates",
        document_id_field="exerciseTemplateId",
        document_create_field="exercise_template",
        response_model=ExerciseTemplateGetResponse,
        model=ExerciseTemplate,
    )
    routine_folders = APIHandler(
        endpoint="routine_folders",
        document_id_field="folderId",
        document_create_field="routine_folder",
        response_model=RoutineFoldersGetResponse,
        model=RoutineFolder,
    )
    routines = RoutinesAPIHandler(
        endpoint="routines",
        document_id_field="routineId",
        document_create_field="routine",
        response_model=RoutineGetResponse,
        model=Routine,
    )
