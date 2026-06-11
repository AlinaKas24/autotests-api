from pathlib import Path

import pytest

from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from fixtures.users import UserFixture

from models.files_model import CreateFileRequestModel, CreateFileResponseModel

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FILE_PATH = PROJECT_ROOT / "testdata" / "files" / "image.png"


class FileFixture(BaseModel):
    request: CreateFileRequestModel
    response: CreateFileResponseModel


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_files(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestModel(upload_file=str(FILE_PATH))
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
