from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_routine_folder_request_body_routine_folder import PostRoutineFolderRequestBodyRoutineFolder


T = TypeVar("T", bound="PostRoutineFolderRequestBody")


@_attrs_define
class PostRoutineFolderRequestBody:
    """
    Attributes:
        routine_folder (Union[Unset, PostRoutineFolderRequestBodyRoutineFolder]):
    """

    routine_folder: Union[Unset, "PostRoutineFolderRequestBodyRoutineFolder"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routine_folder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.routine_folder, Unset):
            routine_folder = self.routine_folder.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routine_folder is not UNSET:
            field_dict["routine_folder"] = routine_folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routine_folder_request_body_routine_folder import PostRoutineFolderRequestBodyRoutineFolder

        d = dict(src_dict)
        _routine_folder = d.pop("routine_folder", UNSET)
        routine_folder: Union[Unset, PostRoutineFolderRequestBodyRoutineFolder]
        if isinstance(_routine_folder, Unset):
            routine_folder = UNSET
        else:
            routine_folder = PostRoutineFolderRequestBodyRoutineFolder.from_dict(_routine_folder)

        post_routine_folder_request_body = cls(
            routine_folder=routine_folder,
        )

        post_routine_folder_request_body.additional_properties = d
        return post_routine_folder_request_body

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
