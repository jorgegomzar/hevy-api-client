from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routine_folder import RoutineFolder


T = TypeVar("T", bound="GetV1RoutineFoldersResponse200")


@_attrs_define
class GetV1RoutineFoldersResponse200:
    """
    Attributes:
        page (Union[Unset, int]): Current page number Default: 1.
        page_count (Union[Unset, int]): Total number of pages Default: 5.
        routine_folders (Union[Unset, list['RoutineFolder']]):
    """

    page: Union[Unset, int] = 1
    page_count: Union[Unset, int] = 5
    routine_folders: Union[Unset, list["RoutineFolder"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        routine_folders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routine_folders, Unset):
            routine_folders = []
            for routine_folders_item_data in self.routine_folders:
                routine_folders_item = routine_folders_item_data.to_dict()
                routine_folders.append(routine_folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if routine_folders is not UNSET:
            field_dict["routine_folders"] = routine_folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routine_folder import RoutineFolder

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_count = d.pop("page_count", UNSET)

        routine_folders = []
        _routine_folders = d.pop("routine_folders", UNSET)
        for routine_folders_item_data in _routine_folders or []:
            routine_folders_item = RoutineFolder.from_dict(routine_folders_item_data)

            routine_folders.append(routine_folders_item)

        get_v1_routine_folders_response_200 = cls(
            page=page,
            page_count=page_count,
            routine_folders=routine_folders,
        )

        get_v1_routine_folders_response_200.additional_properties = d
        return get_v1_routine_folders_response_200

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
