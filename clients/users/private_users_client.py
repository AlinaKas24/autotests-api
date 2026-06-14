from httpx import Response

from clients.api_client import ApiClient
from clients.api_coverage import tracker
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserModel,
)
from models.users_model import GetUserResponseModel, UpdateUserRequestModel
from tools.routes import APIRoutes


class PrivateUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/me")
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/me")

    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def update_user_api(
        self, user_id: str, request: UpdateUserRequestModel
    ) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.USERS}/{user_id}", json=request)

    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

    # Добавили новый метод
    def get_user(self, user_id: str) -> GetUserResponseModel:
        response = self.get_user_api(user_id)
        return GetUserResponseModel.model_validate(response.json())


def get_private_users_client(user: AuthenticationUserModel) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
