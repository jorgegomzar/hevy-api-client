from enum import Enum
from typing import Annotated, Any, Optional

import typer
from rich import print

from hevy_api_client.api.exercise_templates import get_v1_exercise_templates
from hevy_api_client.cli.utils import get_client, print_table
from hevy_api_client.models import GetV1ExerciseTemplatesResponse200
from hevy_api_client.types import Unset

app = typer.Typer(no_args_is_help=True)
client = get_client()


class MuscleGroup(str, Enum):
    abdominals = "abdominals"
    abductors = "abductors"
    biceps = "biceps"
    calves = "calves"
    cardio = "cardio"
    chest = "chest"
    forearms = "forearms"
    full_body = "full_body"
    glutes = "glutes"
    hamstrings = "hamstrings"
    lats = "lats"
    lower_back = "lower_back"
    neck = "neck"
    other = "other"
    quadriceps = "quadriceps"
    shoulders = "shoulders"
    traps = "traps"
    triceps = "triceps"
    upper_back = "upper_back"


class Equipment(str, Enum):
    _none = None
    barbell = "barbell"
    dumbbell = "dumbbell"
    kettlebell = "kettlebell"
    machine = "machine"
    none = "none"
    other = "other"
    plate = "plate"
    resistance_band = "resistance_band"
    suspension = "suspension"


@app.command(name="list")
def list_all(
    muscle_group: Annotated[
        Optional[MuscleGroup],
        typer.Option(
            "-m",
            "--muscle-group",
            help="Filter to show only exercises for the specified muscle group",
        ),
    ] = None,
    equipment: Annotated[
        Optional[Equipment],
        typer.Option(
            "-e",
            "--equipment",
            help="Filter to show only exercises for the specified equipment",
        ),
    ] = None,
) -> None:
    """List all existing exercise templates."""

    exercises: list[dict[str, Any]] = []

    has_more = True
    page = 1

    while has_more:
        res = get_v1_exercise_templates.sync(
            client=client,
            api_key=client.token,  # type: ignore
            page=page,
        )

        if not res or not isinstance(res, GetV1ExerciseTemplatesResponse200):
            break

        has_more = (
            not isinstance(res.exercise_templates, Unset)
            and len(res.exercise_templates) != 0
        )
        page += 1

        if not res.exercise_templates:
            continue

        for exercise in res.exercise_templates:
            if muscle_group is not None and (
                exercise.primary_muscle_group != muscle_group
                or (
                    exercise.secondary_muscle_groups
                    and muscle_group not in exercise.secondary_muscle_groups
                )
            ):
                continue

            if (
                equipment is not None
                and exercise.additional_properties.get("equipment") != equipment
            ):
                continue

            e_dict = exercise.to_dict()
            exercises.append(e_dict)

    if not exercises:
        print("No exercises found")
        raise typer.Exit()

    print_table(
        sorted(
            exercises,
            key=lambda x: (
                x.get("primary_muscle_group") or "",
                x.get("equipment") or "",
            ),
        )
    )
