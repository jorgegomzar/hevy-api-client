from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workout import Workout


T = TypeVar("T", bound="UpdatedWorkout")


@_attrs_define
class UpdatedWorkout:
    """
    Attributes:
        type_ (str): Indicates the type of the event (updated) Example: updated.
        workout (Workout):
    """

    type_: str
    workout: "Workout"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        workout = self.workout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "workout": workout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workout import Workout

        d = dict(src_dict)
        type_ = d.pop("type")

        workout = Workout.from_dict(d.pop("workout"))

        updated_workout = cls(
            type_=type_,
            workout=workout,
        )

        updated_workout.additional_properties = d
        return updated_workout

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
