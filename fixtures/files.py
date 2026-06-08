import pytest

from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from fixtures.users import UserFixture

from models.files_model import CreateFileRequestModel, CreateFileResponseModel


class FileFixture(BaseModel):
    request: CreateFileRequestModel
    response: CreateFileResponseModel


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_files(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestModel(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
