from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_routines_request_set import PostRoutinesRequestSet


T = TypeVar("T", bound="PostRoutinesRequestExercise")


@_attrs_define
class PostRoutinesRequestExercise:
    """
    Attributes:
        exercise_template_id (Union[Unset, str]): The ID of the exercise template. Example: D04AC939.
        superset_id (Union[None, Unset, int]): The ID of the superset.
        rest_seconds (Union[None, Unset, int]): The rest time in seconds. Example: 90.
        notes (Union[None, Unset, str]): Additional notes for the exercise. Example: Stay slow and controlled..
        sets (Union[Unset, list['PostRoutinesRequestSet']]):
    """

    exercise_template_id: Union[Unset, str] = UNSET
    superset_id: Union[None, Unset, int] = UNSET
    rest_seconds: Union[None, Unset, int] = UNSET
    notes: Union[None, Unset, str] = UNSET
    sets: Union[Unset, list["PostRoutinesRequestSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise_template_id = self.exercise_template_id

        superset_id: Union[None, Unset, int]
        if isinstance(self.superset_id, Unset):
            superset_id = UNSET
        else:
            superset_id = self.superset_id

        rest_seconds: Union[None, Unset, int]
        if isinstance(self.rest_seconds, Unset):
            rest_seconds = UNSET
        else:
            rest_seconds = self.rest_seconds

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sets, Unset):
            sets = []
            for sets_item_data in self.sets:
                sets_item = sets_item_data.to_dict()
                sets.append(sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exercise_template_id is not UNSET:
            field_dict["exercise_template_id"] = exercise_template_id
        if superset_id is not UNSET:
            field_dict["superset_id"] = superset_id
        if rest_seconds is not UNSET:
            field_dict["rest_seconds"] = rest_seconds
        if notes is not UNSET:
            field_dict["notes"] = notes
        if sets is not UNSET:
            field_dict["sets"] = sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routines_request_set import PostRoutinesRequestSet

        d = dict(src_dict)
        exercise_template_id = d.pop("exercise_template_id", UNSET)

        def _parse_superset_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        superset_id = _parse_superset_id(d.pop("superset_id", UNSET))

        def _parse_rest_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rest_seconds = _parse_rest_seconds(d.pop("rest_seconds", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        sets = []
        _sets = d.pop("sets", UNSET)
        for sets_item_data in _sets or []:
            sets_item = PostRoutinesRequestSet.from_dict(sets_item_data)

            sets.append(sets_item)

        post_routines_request_exercise = cls(
            exercise_template_id=exercise_template_id,
            superset_id=superset_id,
            rest_seconds=rest_seconds,
            notes=notes,
            sets=sets,
        )

        post_routines_request_exercise.additional_properties = d
        return post_routines_request_exercise

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
