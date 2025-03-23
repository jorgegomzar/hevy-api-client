from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workout_exercises_item import WorkoutExercisesItem


T = TypeVar("T", bound="Workout")


@_attrs_define
class Workout:
    """
    Attributes:
        id (Union[Unset, str]): The workout ID. Example: b459cba5-cd6d-463c-abd6-54f8eafcadcb.
        title (Union[Unset, str]): The workout title. Example: Morning Workout 💪.
        description (Union[Unset, str]): The workout description. Example: Pushed myself to the limit today!.
        start_time (Union[Unset, float]): ISO 8601 timestamp of when the workout was recorded to have started. Example:
            2021-09-14T12:00:00Z.
        end_time (Union[Unset, float]): ISO 8601 timestamp of when the workout was recorded to have ended. Example:
            2021-09-14T12:00:00Z.
        updated_at (Union[Unset, str]): ISO 8601 timestamp of when the workout was last updated. Example:
            2021-09-14T12:00:00Z.
        created_at (Union[Unset, str]): ISO 8601 timestamp of when the workout was created. Example:
            2021-09-14T12:00:00Z.
        exercises (Union[Unset, list['WorkoutExercisesItem']]):
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    start_time: Union[Unset, float] = UNSET
    end_time: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    exercises: Union[Unset, list["WorkoutExercisesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        start_time = self.start_time

        end_time = self.end_time

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
        if description is not UNSET:
            field_dict["description"] = description
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if exercises is not UNSET:
            field_dict["exercises"] = exercises

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workout_exercises_item import WorkoutExercisesItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        exercises = []
        _exercises = d.pop("exercises", UNSET)
        for exercises_item_data in _exercises or []:
            exercises_item = WorkoutExercisesItem.from_dict(exercises_item_data)

            exercises.append(exercises_item)

        workout = cls(
            id=id,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            updated_at=updated_at,
            created_at=created_at,
            exercises=exercises,
        )

        workout.additional_properties = d
        return workout

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
