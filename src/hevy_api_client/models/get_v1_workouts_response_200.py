from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workout import Workout


T = TypeVar("T", bound="GetV1WorkoutsResponse200")


@_attrs_define
class GetV1WorkoutsResponse200:
    """
    Attributes:
        page (Union[Unset, int]): Current page number Example: 1.
        page_count (Union[Unset, int]): Total number of pages Example: 5.
        workouts (Union[Unset, list['Workout']]):
    """

    page: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    workouts: Union[Unset, list["Workout"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        workouts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workouts, Unset):
            workouts = []
            for workouts_item_data in self.workouts:
                workouts_item = workouts_item_data.to_dict()
                workouts.append(workouts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if workouts is not UNSET:
            field_dict["workouts"] = workouts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workout import Workout

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_count = d.pop("page_count", UNSET)

        workouts = []
        _workouts = d.pop("workouts", UNSET)
        for workouts_item_data in _workouts or []:
            workouts_item = Workout.from_dict(workouts_item_data)

            workouts.append(workouts_item)

        get_v1_workouts_response_200 = cls(
            page=page,
            page_count=page_count,
            workouts=workouts,
        )

        get_v1_workouts_response_200.additional_properties = d
        return get_v1_workouts_response_200

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
