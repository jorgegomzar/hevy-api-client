import os
import pytest

from hevy_api_client.client import HevyAPIClient
from hevy_api_client.models import Routine, RoutineFolder


@pytest.fixture()
def client(mocker):
    os.environ["HEVY_API_CLIENT"] = "test_token"
    mocked_client = HevyAPIClient()

    for attr_name in [_ for _ in dir(mocked_client) if not _.startswith("__")]:
        attr = getattr(mocked_client, attr_name)
        attr._request = mocker.Mock(side_effect=[{attr.document_create_field: True}])
        attr.model = mocker.Mock()

    return mocked_client


@pytest.mark.parametrize(
    "doc, attr, attr_data",
    [
        (RoutineFolder(title="test"), "routine_folders", "routine_folder"),
        (Routine(title="test", folder_id=1), "routines", "routine"),
    ]
)
def test_routine_directory_creation(client: HevyAPIClient, doc, attr: str, attr_data: str):
    _ = getattr(client, attr).create(doc)

    getattr(client, attr)._request.assert_called_once_with(
        method="POST",
        data={attr_data: doc.model_dump(exclude_none=True)},
    )
