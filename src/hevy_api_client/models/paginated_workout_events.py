from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deleted_workout import DeletedWorkout
    from ..models.updated_workout import UpdatedWorkout


T = TypeVar("T", bound="PaginatedWorkoutEvents")


@_attrs_define
class PaginatedWorkoutEvents:
    """
    Attributes:
        page (int): The current page number Example: 1.
        page_count (int): The total number of pages available Example: 5.
        events (list[Union['DeletedWorkout', 'UpdatedWorkout']]): An array of workout events (either updated or deleted)
    """

    page: int
    page_count: int
    events: list[Union["DeletedWorkout", "UpdatedWorkout"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.updated_workout import UpdatedWorkout

        page = self.page

        page_count = self.page_count

        events = []
        for events_item_data in self.events:
            events_item: dict[str, Any]
            if isinstance(events_item_data, UpdatedWorkout):
                events_item = events_item_data.to_dict()
            else:
                events_item = events_item_data.to_dict()

            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "page_count": page_count,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deleted_workout import DeletedWorkout
        from ..models.updated_workout import UpdatedWorkout

        d = dict(src_dict)
        page = d.pop("page")

        page_count = d.pop("page_count")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:

            def _parse_events_item(data: object) -> Union["DeletedWorkout", "UpdatedWorkout"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    events_item_type_0 = UpdatedWorkout.from_dict(data)

                    return events_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                events_item_type_1 = DeletedWorkout.from_dict(data)

                return events_item_type_1

            events_item = _parse_events_item(events_item_data)

            events.append(events_item)

        paginated_workout_events = cls(
            page=page,
            page_count=page_count,
            events=events,
        )

        paginated_workout_events.additional_properties = d
        return paginated_workout_events

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
