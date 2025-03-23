from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_workout_events import PaginatedWorkoutEvents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 5,
    since: Union[Unset, str] = "1970-01-01T00:00:00Z",
    api_key: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["api-key"] = api_key

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workouts/events",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaginatedWorkoutEvents]]:
    if response.status_code == 200:
        response_200 = PaginatedWorkoutEvents.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PaginatedWorkoutEvents]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 5,
    since: Union[Unset, str] = "1970-01-01T00:00:00Z",
    api_key: UUID,
) -> Response[Union[Any, PaginatedWorkoutEvents]]:
    """Retrieve a paged list of workout events (updates or deletes) since a given date. Events are ordered
    from newest to oldest. The intention is to allow clients to keep their local cache of workouts up to
    date without having to fetch the entire list of workouts.

     Returns a paginated array of workout events, indicating updates or deletions.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 5.
        since (Union[Unset, str]):  Default: '1970-01-01T00:00:00Z'.
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedWorkoutEvents]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        since=since,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 5,
    since: Union[Unset, str] = "1970-01-01T00:00:00Z",
    api_key: UUID,
) -> Optional[Union[Any, PaginatedWorkoutEvents]]:
    """Retrieve a paged list of workout events (updates or deletes) since a given date. Events are ordered
    from newest to oldest. The intention is to allow clients to keep their local cache of workouts up to
    date without having to fetch the entire list of workouts.

     Returns a paginated array of workout events, indicating updates or deletions.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 5.
        since (Union[Unset, str]):  Default: '1970-01-01T00:00:00Z'.
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaginatedWorkoutEvents]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        since=since,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 5,
    since: Union[Unset, str] = "1970-01-01T00:00:00Z",
    api_key: UUID,
) -> Response[Union[Any, PaginatedWorkoutEvents]]:
    """Retrieve a paged list of workout events (updates or deletes) since a given date. Events are ordered
    from newest to oldest. The intention is to allow clients to keep their local cache of workouts up to
    date without having to fetch the entire list of workouts.

     Returns a paginated array of workout events, indicating updates or deletions.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 5.
        since (Union[Unset, str]):  Default: '1970-01-01T00:00:00Z'.
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedWorkoutEvents]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        since=since,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 5,
    since: Union[Unset, str] = "1970-01-01T00:00:00Z",
    api_key: UUID,
) -> Optional[Union[Any, PaginatedWorkoutEvents]]:
    """Retrieve a paged list of workout events (updates or deletes) since a given date. Events are ordered
    from newest to oldest. The intention is to allow clients to keep their local cache of workouts up to
    date without having to fetch the entire list of workouts.

     Returns a paginated array of workout events, indicating updates or deletions.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 5.
        since (Union[Unset, str]):  Default: '1970-01-01T00:00:00Z'.
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaginatedWorkoutEvents]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            since=since,
            api_key=api_key,
        )
    ).parsed
