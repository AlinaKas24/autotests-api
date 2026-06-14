from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.api_coverage import tracker
from clients.public_http_builder import get_public_http_client
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from tools.routes import APIRoutes


class PublicUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}")
    def create_user_api(
        self,
        request: CreateUserRequestSchema,
    ) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.USERS}", json=request.model_dump(by_alias=True))

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
