from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutineFolder")


@_attrs_define
class RoutineFolder:
    """
    Attributes:
        id (Union[Unset, float]): The routine folder ID. Example: 42.
        index (Union[Unset, float]): The routine folder index. Describes the order of the folder in the list. Example:
            1.
        title (Union[Unset, str]): The routine folder title. Example: Push Pull 🏋️‍♂️.
        updated_at (Union[Unset, str]): ISO 8601 timestamp of when the folder was last updated. Example:
            2021-09-14T12:00:00Z.
        created_at (Union[Unset, str]): ISO 8601 timestamp of when the folder was created. Example:
            2021-09-14T12:00:00Z.
    """

    id: Union[Unset, float] = UNSET
    index: Union[Unset, float] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index = self.index

        title = self.title

        updated_at = self.updated_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        routine_folder = cls(
            id=id,
            index=index,
            title=title,
            updated_at=updated_at,
            created_at=created_at,
        )

        routine_folder.additional_properties = d
        return routine_folder

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
