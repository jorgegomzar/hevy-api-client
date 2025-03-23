from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_routine_folder_request_body import PostRoutineFolderRequestBody
from ...models.post_v1_routine_folders_response_400 import PostV1RoutineFoldersResponse400
from ...models.routine_folder import RoutineFolder
from ...types import Response


def _get_kwargs(
    *,
    body: PostRoutineFolderRequestBody,
    api_key: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["api-key"] = api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/routine_folders",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    if response.status_code == 201:
        response_201 = RoutineFolder.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = PostV1RoutineFoldersResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostRoutineFolderRequestBody,
    api_key: UUID,
) -> Response[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    """Create a new routine folder. The folder will be created at index 0, and all other folders will have
    their indexes incremented.

    Args:
        api_key (UUID):
        body (PostRoutineFolderRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostRoutineFolderRequestBody,
    api_key: UUID,
) -> Optional[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    """Create a new routine folder. The folder will be created at index 0, and all other folders will have
    their indexes incremented.

    Args:
        api_key (UUID):
        body (PostRoutineFolderRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostV1RoutineFoldersResponse400, RoutineFolder]
    """

    return sync_detailed(
        client=client,
        body=body,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostRoutineFolderRequestBody,
    api_key: UUID,
) -> Response[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    """Create a new routine folder. The folder will be created at index 0, and all other folders will have
    their indexes incremented.

    Args:
        api_key (UUID):
        body (PostRoutineFolderRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostRoutineFolderRequestBody,
    api_key: UUID,
) -> Optional[Union[PostV1RoutineFoldersResponse400, RoutineFolder]]:
    """Create a new routine folder. The folder will be created at index 0, and all other folders will have
    their indexes incremented.

    Args:
        api_key (UUID):
        body (PostRoutineFolderRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostV1RoutineFoldersResponse400, RoutineFolder]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            api_key=api_key,
        )
    ).parsed
