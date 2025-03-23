from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1WorkoutsCountResponse200")


@_attrs_define
class GetV1WorkoutsCountResponse200:
    """
    Attributes:
        workout_count (Union[Unset, int]): The total number of workouts Default: 42.
    """

    workout_count: Union[Unset, int] = 42
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workout_count = self.workout_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workout_count is not UNSET:
            field_dict["workout_count"] = workout_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workout_count = d.pop("workout_count", UNSET)

        get_v1_workouts_count_response_200 = cls(
            workout_count=workout_count,
        )

        get_v1_workouts_count_response_200.additional_properties = d
        return get_v1_workouts_count_response_200

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
