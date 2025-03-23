from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routine_exercises_item import RoutineExercisesItem


T = TypeVar("T", bound="Routine")


@_attrs_define
class Routine:
    """
    Attributes:
        id (Union[Unset, str]): The routine ID. Example: b459cba5-cd6d-463c-abd6-54f8eafcadcb.
        title (Union[Unset, str]): The routine title. Example: Upper Body 💪.
        folder_id (Union[None, Unset, float]): The routine folder ID. Example: 42.
        updated_at (Union[Unset, str]): ISO 8601 timestamp of when the routine was last updated. Example:
            2021-09-14T12:00:00Z.
        created_at (Union[Unset, str]): ISO 8601 timestamp of when the routine was created. Example:
            2021-09-14T12:00:00Z.
        exercises (Union[Unset, list['RoutineExercisesItem']]):
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    folder_id: Union[None, Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    exercises: Union[Unset, list["RoutineExercisesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        folder_id: Union[None, Unset, float]
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        updated_at = self.updated_at

        created_at = self.created_at

        exercises: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exercises, Unset):
            exercises = []
            for exercises_item_data in self.exercises:
                exercises_item = exercises_item_data.to_dict()
                exercises.append(exercises_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if exercises is not UNSET:
            field_dict["exercises"] = exercises

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routine_exercises_item import RoutineExercisesItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        def _parse_folder_id(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        exercises = []
        _exercises = d.pop("exercises", UNSET)
        for exercises_item_data in _exercises or []:
            exercises_item = RoutineExercisesItem.from_dict(exercises_item_data)

            exercises.append(exercises_item)

        routine = cls(
            id=id,
            title=title,
            folder_id=folder_id,
            updated_at=updated_at,
            created_at=created_at,
            exercises=exercises,
        )

        routine.additional_properties = d
        return routine

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
