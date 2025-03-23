from typing import Annotated

import typer

from hevy_api_client.api.routine_folders import (
    get_v1_routine_folders,
    post_v1_routine_folders,
)
from hevy_api_client.cli.utils import get_client, print_table
from hevy_api_client.models import (
    PostRoutineFolderRequestBody,
    PostRoutineFolderRequestBodyRoutineFolder,
    PostV1RoutineFoldersResponse400,
    RoutineFolder,
)
from hevy_api_client.types import Unset

app = typer.Typer(no_args_is_help=True)
client = get_client()


@app.command(name="list")
def list_all() -> None:
    """Lists all existing routine folders."""

    routine_folders: list[RoutineFolder] = []

    has_more = True
    page = 1

    while has_more:
        if not (
            res := get_v1_routine_folders.sync(
                client=client,
                api_key=client.token,  # type: ignore
                page=page,
            )
        ):
            break

        has_more = (
            not isinstance(res.routine_folders, Unset) and len(res.routine_folders) != 0
        )
        page += 1

        if res.routine_folders:
            routine_folders.extend(res.routine_folders)

    if not routine_folders:
        print("No routine folders found")
        raise typer.Exit()

    print_table([rf.to_dict() for rf in routine_folders])


@app.command()
def create(
    title: Annotated[str, typer.Argument(help="Title for the new routine folder")],
):
    """Creates a new routine folder with the provided title and prints it."""

    res = post_v1_routine_folders.sync(
        client=client,
        api_key=client.token,  # type: ignore
        body=PostRoutineFolderRequestBody(
            routine_folder=PostRoutineFolderRequestBodyRoutineFolder(title)
        ),
    )

    if not res or not isinstance(res, RoutineFolder):
        print("Could not get a valid response")
        if isinstance(res, PostV1RoutineFoldersResponse400):
            print(res.error)
        raise typer.Exit(-1)

    print_table([res.to_dict()["routine_folder"]])
