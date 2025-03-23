from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_routines_request_body_routine import PostRoutinesRequestBodyRoutine


T = TypeVar("T", bound="PostRoutinesRequestBody")


@_attrs_define
class PostRoutinesRequestBody:
    """
    Attributes:
        routine (Union[Unset, PostRoutinesRequestBodyRoutine]):
    """

    routine: Union[Unset, "PostRoutinesRequestBodyRoutine"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routine: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.routine, Unset):
            routine = self.routine.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routine is not UNSET:
            field_dict["routine"] = routine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routines_request_body_routine import PostRoutinesRequestBodyRoutine

        d = dict(src_dict)
        _routine = d.pop("routine", UNSET)
        routine: Union[Unset, PostRoutinesRequestBodyRoutine]
        if isinstance(_routine, Unset):
            routine = UNSET
        else:
            routine = PostRoutinesRequestBodyRoutine.from_dict(_routine)

        post_routines_request_body = cls(
            routine=routine,
        )

        post_routines_request_body.additional_properties = d
        return post_routines_request_body

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
