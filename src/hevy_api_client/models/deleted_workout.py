from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletedWorkout")


@_attrs_define
class DeletedWorkout:
    """
    Attributes:
        type_ (str): Indicates the type of the event (deleted) Example: deleted.
        id (str): The unique identifier of the deleted workout Example: efe6801c-4aee-4959-bcdd-fca3f272821b.
        deleted_at (Union[Unset, str]): A date string indicating when the workout was deleted Example:
            2021-09-13T12:00:00Z.
    """

    type_: str
    id: str
    deleted_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        deleted_at = d.pop("deleted_at", UNSET)

        deleted_workout = cls(
            type_=type_,
            id=id,
            deleted_at=deleted_at,
        )

        deleted_workout.additional_properties = d
        return deleted_workout

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
