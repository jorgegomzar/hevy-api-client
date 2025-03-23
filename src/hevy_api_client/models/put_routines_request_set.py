from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_routines_request_set_type import PutRoutinesRequestSetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutRoutinesRequestSet")


@_attrs_define
class PutRoutinesRequestSet:
    """
    Attributes:
        type_ (Union[Unset, PutRoutinesRequestSetType]): The type of the set. Example: normal.
        weight_kg (Union[None, Unset, float]): The weight in kilograms. Example: 100.
        reps (Union[None, Unset, int]): The number of repetitions. Example: 10.
        distance_meters (Union[None, Unset, int]): The distance in meters.
        duration_seconds (Union[None, Unset, int]): The duration in seconds.
        custom_metric (Union[None, Unset, float]): A custom metric for the set. Currently used for steps and floors.
    """

    type_: Union[Unset, PutRoutinesRequestSetType] = UNSET
    weight_kg: Union[None, Unset, float] = UNSET
    reps: Union[None, Unset, int] = UNSET
    distance_meters: Union[None, Unset, int] = UNSET
    duration_seconds: Union[None, Unset, int] = UNSET
    custom_metric: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        weight_kg: Union[None, Unset, float]
        if isinstance(self.weight_kg, Unset):
            weight_kg = UNSET
        else:
            weight_kg = self.weight_kg

        reps: Union[None, Unset, int]
        if isinstance(self.reps, Unset):
            reps = UNSET
        else:
            reps = self.reps

        distance_meters: Union[None, Unset, int]
        if isinstance(self.distance_meters, Unset):
            distance_meters = UNSET
        else:
            distance_meters = self.distance_meters

        duration_seconds: Union[None, Unset, int]
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        custom_metric: Union[None, Unset, float]
        if isinstance(self.custom_metric, Unset):
            custom_metric = UNSET
        else:
            custom_metric = self.custom_metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if weight_kg is not UNSET:
            field_dict["weight_kg"] = weight_kg
        if reps is not UNSET:
            field_dict["reps"] = reps
        if distance_meters is not UNSET:
            field_dict["distance_meters"] = distance_meters
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if custom_metric is not UNSET:
            field_dict["custom_metric"] = custom_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PutRoutinesRequestSetType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PutRoutinesRequestSetType(_type_)

        def _parse_weight_kg(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight_kg = _parse_weight_kg(d.pop("weight_kg", UNSET))

        def _parse_reps(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reps = _parse_reps(d.pop("reps", UNSET))

        def _parse_distance_meters(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_meters = _parse_distance_meters(d.pop("distance_meters", UNSET))

        def _parse_duration_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_custom_metric(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        custom_metric = _parse_custom_metric(d.pop("custom_metric", UNSET))

        put_routines_request_set = cls(
            type_=type_,
            weight_kg=weight_kg,
            reps=reps,
            distance_meters=distance_meters,
            duration_seconds=duration_seconds,
            custom_metric=custom_metric,
        )

        put_routines_request_set.additional_properties = d
        return put_routines_request_set

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
