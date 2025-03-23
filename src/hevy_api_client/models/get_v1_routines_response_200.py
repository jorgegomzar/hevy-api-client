from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routine import Routine


T = TypeVar("T", bound="GetV1RoutinesResponse200")


@_attrs_define
class GetV1RoutinesResponse200:
    """
    Attributes:
        page (Union[Unset, int]): Current page number Example: 1.
        page_count (Union[Unset, int]): Total number of pages Example: 5.
        routines (Union[Unset, list['Routine']]):
    """

    page: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    routines: Union[Unset, list["Routine"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        routines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routines, Unset):
            routines = []
            for routines_item_data in self.routines:
                routines_item = routines_item_data.to_dict()
                routines.append(routines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if routines is not UNSET:
            field_dict["routines"] = routines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routine import Routine

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_count = d.pop("page_count", UNSET)

        routines = []
        _routines = d.pop("routines", UNSET)
        for routines_item_data in _routines or []:
            routines_item = Routine.from_dict(routines_item_data)

            routines.append(routines_item)

        get_v1_routines_response_200 = cls(
            page=page,
            page_count=page_count,
            routines=routines,
        )

        get_v1_routines_response_200.additional_properties = d
        return get_v1_routines_response_200

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
