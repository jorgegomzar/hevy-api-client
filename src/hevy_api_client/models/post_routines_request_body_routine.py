from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_routines_request_exercise import PostRoutinesRequestExercise


T = TypeVar("T", bound="PostRoutinesRequestBodyRoutine")


@_attrs_define
class PostRoutinesRequestBodyRoutine:
    """
    Attributes:
        title (Union[Unset, str]): The title of the routine. Example: April Leg Day 🔥.
        folder_id (Union[None, Unset, float]): The folder id the routine should be added to. Pass null to insert the
            routine into default "My Routines" folder
        notes (Union[Unset, str]): Additional notes for the routine. Example: Focus on form over weight. Remember to
            stretch..
        exercises (Union[Unset, list['PostRoutinesRequestExercise']]):
    """

    title: Union[Unset, str] = UNSET
    folder_id: Union[None, Unset, float] = UNSET
    notes: Union[Unset, str] = UNSET
    exercises: Union[Unset, list["PostRoutinesRequestExercise"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        folder_id: Union[None, Unset, float]
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        notes = self.notes

        exercises: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exercises, Unset):
            exercises = []
            for exercises_item_data in self.exercises:
                exercises_item = exercises_item_data.to_dict()
                exercises.append(exercises_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if exercises is not UNSET:
            field_dict["exercises"] = exercises

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routines_request_exercise import PostRoutinesRequestExercise

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_folder_id(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

        notes = d.pop("notes", UNSET)

        exercises = []
        _exercises = d.pop("exercises", UNSET)
        for exercises_item_data in _exercises or []:
            exercises_item = PostRoutinesRequestExercise.from_dict(exercises_item_data)

            exercises.append(exercises_item)

        post_routines_request_body_routine = cls(
            title=title,
            folder_id=folder_id,
            notes=notes,
            exercises=exercises,
        )

        post_routines_request_body_routine.additional_properties = d
        return post_routines_request_body_routine

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
