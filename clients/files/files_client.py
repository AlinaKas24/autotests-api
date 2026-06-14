from pathlib import Path

from httpx import Response

from clients.api_client import ApiClient
from clients.api_coverage import tracker
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserModel,
)
from models.files_model import CreateFileRequestModel, CreateFileResponseModel
from tools.routes import APIRoutes


class FilesClient(ApiClient):
    """
    Клиент для работы с приватными эндпоинтами
    """

    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.delete(f"{APIRoutes.FILES}/{file_id}")

    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}")
    def create_file_api(self, request: CreateFileRequestModel) -> Response:
        file_path = Path(request.upload_file).resolve()
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post(
            f"{APIRoutes.FILES}",
            data=request.model_dump(by_alias=True),
            files={"upload_file": open(file_path, "rb")},
        )

    def create_file(self, request: CreateFileRequestModel) -> CreateFileResponseModel:
        response = self.create_file_api(request)
        return CreateFileResponseModel.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserModel) -> FilesClient:
    return FilesClient(client=get_private_http_client(user))
