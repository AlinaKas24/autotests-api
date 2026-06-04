from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from models.authentication_model import (
    LoginRequestModel,
    RefreshRequestModel,
    LoginResponseModel,
)


class AuthenticationClient(ApiClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestModel) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post(
            "/api/v1/authentication/login", json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestModel) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/refresh", json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestModel) -> LoginResponseModel:
        response = self.login_api(request)
        return LoginResponseModel.model_validate(response.json())


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
