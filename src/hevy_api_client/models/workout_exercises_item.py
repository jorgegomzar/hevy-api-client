from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workout_exercises_item_sets_item import WorkoutExercisesItemSetsItem


T = TypeVar("T", bound="WorkoutExercisesItem")


@_attrs_define
class WorkoutExercisesItem:
    """
    Attributes:
        index (Union[Unset, float]): Index indicating the order of the exercise in the workout.
        title (Union[Unset, str]): Title of the exercise Example: Bench Press (Barbell).
        notes (Union[Unset, str]): Notes on the exercise Example: Paid closer attention to form today. Felt great!.
        exercise_template_id (Union[Unset, str]): The id of the exercise template. This can be used to fetch the
            exercise template. Example: 05293BCA.
        supersets_id (Union[None, Unset, float]): The id of the superset that the exercise belongs to. A value of null
            indicates the exercise is not part of a superset.
        sets (Union[Unset, list['WorkoutExercisesItemSetsItem']]):
    """

    index: Union[Unset, float] = UNSET
    title: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    exercise_template_id: Union[Unset, str] = UNSET
    supersets_id: Union[None, Unset, float] = UNSET
    sets: Union[Unset, list["WorkoutExercisesItemSetsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        title = self.title

        notes = self.notes

        exercise_template_id = self.exercise_template_id

        supersets_id: Union[None, Unset, float]
        if isinstance(self.supersets_id, Unset):
            supersets_id = UNSET
        else:
            supersets_id = self.supersets_id

        sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sets, Unset):
            sets = []
            for sets_item_data in self.sets:
                sets_item = sets_item_data.to_dict()
                sets.append(sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if exercise_template_id is not UNSET:
            field_dict["exercise_template_id"] = exercise_template_id
        if supersets_id is not UNSET:
            field_dict["supersets_id"] = supersets_id
        if sets is not UNSET:
            field_dict["sets"] = sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workout_exercises_item_sets_item import WorkoutExercisesItemSetsItem

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        title = d.pop("title", UNSET)

        notes = d.pop("notes", UNSET)

        exercise_template_id = d.pop("exercise_template_id", UNSET)

        def _parse_supersets_id(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supersets_id = _parse_supersets_id(d.pop("supersets_id", UNSET))

        sets = []
        _sets = d.pop("sets", UNSET)
        for sets_item_data in _sets or []:
            sets_item = WorkoutExercisesItemSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        workout_exercises_item = cls(
            index=index,
            title=title,
            notes=notes,
            exercise_template_id=exercise_template_id,
            supersets_id=supersets_id,
            sets=sets,
        )

        workout_exercises_item.additional_properties = d
        return workout_exercises_item

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
