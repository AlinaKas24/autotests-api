import allure

from models.authentication_model import LoginRequestModel, LoginResponseModel
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from tools.assertions.base import assert_equal

from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(
    request: CreateUserRequestSchema, response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create user response")
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check login user response")
def assert_login_user_response(
    request: LoginRequestModel, response: LoginResponseModel
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check login user response")
    assert_equal(response.user.email, request.email, "email")
