from dataclasses import dataclass
import json
import os
from typing import Any, Iterator, Optional, Type, TypeVar, Union
from pydantic import ValidationError
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

    def create(self, doc: T) -> T:
        req_params = {
            "method": "POST",
            "data": {self.document_create_field: doc.model_dump(exclude_none=True)},
        }

        res = self._request(**req_params)

        try:
            return self.model.model_validate(res[self.document_create_field])
        except ValidationError as e:
            raise HevyAPIException(f"Could not validate response for {self.model.__name__} creation.\nValidationError: {e}\nResponse: {res}")

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


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    client = HevyAPIClient()
    routine_folder = client.routine_folders.create(RoutineFolder(title="Testing Hevy API"))

    assert routine_folder.id is not None
    print(f"{routine_folder=}")

    routine = client.routines.create(Routine(title="Testing Hevy API routine", folder_id=routine_folder.id))
    print(f"{routine=}")
