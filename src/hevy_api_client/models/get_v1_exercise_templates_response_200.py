from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_template import ExerciseTemplate


T = TypeVar("T", bound="GetV1ExerciseTemplatesResponse200")


@_attrs_define
class GetV1ExerciseTemplatesResponse200:
    """
    Attributes:
        page (Union[Unset, int]): Current page number Default: 1.
        page_count (Union[Unset, int]): Total number of pages Default: 5.
        exercise_templates (Union[Unset, list['ExerciseTemplate']]):
    """

    page: Union[Unset, int] = 1
    page_count: Union[Unset, int] = 5
    exercise_templates: Union[Unset, list["ExerciseTemplate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        exercise_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exercise_templates, Unset):
            exercise_templates = []
            for exercise_templates_item_data in self.exercise_templates:
                exercise_templates_item = exercise_templates_item_data.to_dict()
                exercise_templates.append(exercise_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if exercise_templates is not UNSET:
            field_dict["exercise_templates"] = exercise_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_template import ExerciseTemplate

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_count = d.pop("page_count", UNSET)

        exercise_templates = []
        _exercise_templates = d.pop("exercise_templates", UNSET)
        for exercise_templates_item_data in _exercise_templates or []:
            exercise_templates_item = ExerciseTemplate.from_dict(exercise_templates_item_data)

            exercise_templates.append(exercise_templates_item)

        get_v1_exercise_templates_response_200 = cls(
            page=page,
            page_count=page_count,
            exercise_templates=exercise_templates,
        )

        get_v1_exercise_templates_response_200.additional_properties = d
        return get_v1_exercise_templates_response_200

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
