from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field


class Document(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class RoutineFolder(Document):
    id: Optional[int] = None
    title: str
    index: Optional[int] = None


class Set(Document):
    index: int
    set_type: str
    weight_kg: Optional[float] = None
    reps: Optional[int] = None
    distance_meters: Optional[float] = None
    duration_seconds: Optional[float] = None
    rpe: Optional[float] = None


class Exercise(Document):
    index: int
    title: str
    notes: Optional[str] = None
    exercise_template_id: str
    supersets_id: Optional[int] = None
    sets: list[Set]


class Routine(Document):
    id: Optional[str] = None
    title: str
    folder_id: int
    exercises: list[Exercise] = Field(..., default_factory=list)


class Workout(Document):
    id: Optional[str] = None
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    exercises: list[Exercise]


class ExerciseTemplate(Document):
    id: Optional[str] = None
    title: str
    type: str
    primary_muscle_group: str
    secondary_muscle_groups: list[str]
    is_custom: bool


class GetResponse(BaseModel, ABC):
    page: int
    page_count: int

    @abstractmethod
    def get_fields(self) -> list:
        ...


class RoutineFoldersGetResponse(GetResponse):
    routine_folders: list[RoutineFolder]

    def get_fields(self) -> list:
        return self.routine_folders


class RoutineGetResponse(GetResponse):
    routines: list[Routine]

    def get_fields(self) -> list:
        return self.routines


class WorkoutGetResponse(GetResponse):
    workouts: list[Workout]

    def get_fields(self) -> list:
        return self.workouts


class ExerciseTemplateGetResponse(GetResponse):
    exercise_templates: list[ExerciseTemplate]

    def get_fields(self) -> list:
        return self.exercise_templates


Model = Union[RoutineFolder, Routine, Exercise, Set, Workout, ExerciseTemplate]
ResponseModel = Union[RoutineFoldersGetResponse, RoutineGetResponse, WorkoutGetResponse, ExerciseTemplateGetResponse]
