from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseTemplate")


@_attrs_define
class ExerciseTemplate:
    """
    Attributes:
        id (Union[Unset, str]): The exercise template ID. Example: b459cba5-cd6d-463c-abd6-54f8eafcadcb.
        title (Union[Unset, str]): The exercise title. Example: Bench Press (Barbell).
        type_ (Union[Unset, str]): The exercise type. Example: weight_reps.
        primary_muscle_group (Union[Unset, str]): The primary muscle group of the exercise. Example: weight_reps.
        secondary_muscle_groups (Union[Unset, list[str]]): The secondary muscle groups of the exercise.
        is_custom (Union[Unset, bool]): A boolean indicating whether the exercise is a custom exercise.
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    primary_muscle_group: Union[Unset, str] = UNSET
    secondary_muscle_groups: Union[Unset, list[str]] = UNSET
    is_custom: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        type_ = self.type_

        primary_muscle_group = self.primary_muscle_group

        secondary_muscle_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.secondary_muscle_groups, Unset):
            secondary_muscle_groups = self.secondary_muscle_groups

        is_custom = self.is_custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if primary_muscle_group is not UNSET:
            field_dict["primary_muscle_group"] = primary_muscle_group
        if secondary_muscle_groups is not UNSET:
            field_dict["secondary_muscle_groups"] = secondary_muscle_groups
        if is_custom is not UNSET:
            field_dict["is_custom"] = is_custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        primary_muscle_group = d.pop("primary_muscle_group", UNSET)

        secondary_muscle_groups = cast(list[str], d.pop("secondary_muscle_groups", UNSET))

        is_custom = d.pop("is_custom", UNSET)

        exercise_template = cls(
            id=id,
            title=title,
            type_=type_,
            primary_muscle_group=primary_muscle_group,
            secondary_muscle_groups=secondary_muscle_groups,
            is_custom=is_custom,
        )

        exercise_template.additional_properties = d
        return exercise_template

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
