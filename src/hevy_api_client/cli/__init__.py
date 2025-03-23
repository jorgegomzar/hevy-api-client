import typer

from hevy_api_client.cli import exercise_templates, routine_folders, routines

app = typer.Typer(no_args_is_help=True)
app.add_typer(routine_folders.app, name="routine_folders")
app.add_typer(routines.app, name="routines")
app.add_typer(exercise_templates.app, name="exercise_templates")


def cli_entrypoint():
    app()
