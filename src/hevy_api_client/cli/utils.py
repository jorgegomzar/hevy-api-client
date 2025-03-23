import os
from typing import Any

from rich import print
from rich.console import Console
from rich.table import Table

from hevy_api_client.client import AuthenticatedClient


class HevyAPIError(ValueError): ...


def get_client() -> AuthenticatedClient:
    token = os.getenv("HEVY_API_TOKEN")

    if not token:
        raise HevyAPIError("Token cannot be missing")

    return AuthenticatedClient(token)


def print_table(data: list[dict[str, Any]]) -> None:
    console = Console()

    table = Table(*data[0].keys())

    # ensure the ID is always visible
    table.columns[0].no_wrap = True

    for row in data:
        table.add_row(*map(str, row.values()))

    console.print(table)
    print(f"Total: {len(data)}")
