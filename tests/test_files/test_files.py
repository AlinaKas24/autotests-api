from http import HTTPStatus
from pathlib import Path

import pytest

from clients.errors_model import (
    ValidationErrorResponseModel,
    NotFoundErrorResponseModel,
    IncorrectFileIdErrorResponseModel,
)
from clients.files.files_client import FilesClient
from fixtures.files import FileFixture
from models.files_model import (
    CreateFileRequestModel,
    CreateFileResponseModel,
    GetFileResponseModel,
)
from tools.assertions.base import assert_status_code
from tools.assertions.errors import assert_incorrect_file_id_errors_response
from tools.assertions.files import (
    assert_create_file_with_empy_file_name_response,
    assert_create_file_with_empy_directory_response,
    assert_delete_file_not_found_response,
    assert_get_file_with_incorrect_file_id_response,
)
from tools.assertions.schema import validate_json_schema

ROOT_DIR = Path(__file__).resolve().parents[2]

file_path = ROOT_DIR / "testdata" / "files" / "image.png"


@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestModel(upload_file=str(file_path))
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseModel.model_validate_json(response.text)
        assert response.status_code == HTTPStatus.OK

    def test_get_file(self, files_client: FilesClient, function_files: FileFixture):
        response = files_client.get_file_api(file_id=function_files.response.file.id)
        response_data = GetFileResponseModel.model_validate_json(response.text)
        print(response_data)

    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestModel(filename="", upload_file=str(file_path))
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empy_file_name_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestModel(directory="", upload_file=str(file_path))
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empy_directory_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_file(self, files_client: FilesClient):
        request = CreateFileRequestModel(upload_file=str(file_path))
        response = files_client.create_file_api(request)
        file_id = response.json().get("file").get("id")
        print(file_id)
        CreateFileResponseModel.model_validate_json(response.text)
        response_delete = files_client.delete_file_api(file_id=file_id)
        assert_status_code(response_delete.status_code, HTTPStatus.OK)
        response_get = files_client.get_file_api(file_id=file_id)
        response_data = NotFoundErrorResponseModel.model_validate_json(
            response_get.text
        )
        print(response_get.json())
        assert_status_code(response_get.status_code, HTTPStatus.NOT_FOUND)
        assert_delete_file_not_found_response(response_data)
        validate_json_schema(response_get.json(), response_data.model_json_schema())

    def test_incorrect_file_id_file(self, files_client: FilesClient):
        response_get = files_client.get_file_api(file_id="file_id")
        response_data = IncorrectFileIdErrorResponseModel.model_validate_json(
            response_get.text
        )
        assert_status_code(response_get.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)
        validate_json_schema(response_get.json(), response_data.model_json_schema())
