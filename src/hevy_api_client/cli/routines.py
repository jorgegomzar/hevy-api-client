from typing import Annotated, Any, Optional

import typer
from rich import print

from hevy_api_client.api.routines import get_v1_routines, post_v1_routines
from hevy_api_client.cli.utils import get_client, print_table
from hevy_api_client.models import (
    GetV1RoutinesResponse200,
    PostRoutinesRequestBody,
    PostRoutinesRequestBodyRoutine,
    PostRoutinesRequestExercise,
    PostV1RoutinesResponse400,
    PostV1RoutinesResponse403,
    Routine,
)
from hevy_api_client.types import Unset

app = typer.Typer(no_args_is_help=True)
client = get_client()


@app.command(name="list")
def list_all(
    folder_id: Annotated[
        Optional[int],
        typer.Option("-F", "--folder", help="Filter to show only from this folder id"),
    ] = None,
):
    """List all existing routines. If -F/--folder is provided
    then only the routines for that folder will be shown"""

    routines: list[dict[str, Any]] = []

    has_more = True
    page = 1

    while has_more:
        res = get_v1_routines.sync(
            client=client,
            api_key=client.token,  # type: ignore
            page=page,
        )

        if not res or not isinstance(res, GetV1RoutinesResponse200):
            break

        has_more = not isinstance(res.routines, Unset) and len(res.routines) != 0
        page += 1

        if not res.routines:
            continue

        for routine in res.routines:
            if folder_id is not None and routine.folder_id != folder_id:
                continue

            r_dict = routine.to_dict()
            del r_dict["exercises"]
            routines.append(r_dict)

    if not routines:
        print("No routines found")
        raise typer.Exit()

    print_table(
        sorted(
            routines,
            key=lambda x: (str(x.get("folder_id") or ""), x.get("title") or ""),
        )
    )


# @app.command()
# TODO: implement
def create(title: str, folder_id: int):
    """Create a new routine"""

    res = post_v1_routines.sync(
        client=client,
        api_key=client.token,  # type: ignore
        body=PostRoutinesRequestBody(
            routine=PostRoutinesRequestBodyRoutine(
                title=title,
                folder_id=folder_id,
                exercises=[
                    PostRoutinesRequestExercise(
                        exercise_template_id="D04AC939",
                        sets=[
                            # PostRoutinesRequestSet()
                        ],
                    )
                ],
            )
        ),
    )

    if not res or not isinstance(res, Routine):
        print("ERROR")
        if isinstance(res, (PostV1RoutinesResponse400, PostV1RoutinesResponse403)):
            print({res.error})
        raise typer.Exit(-1)

    list_all(folder_id)
