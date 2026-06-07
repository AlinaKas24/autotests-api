from http import HTTPStatus

import pytest

from api_client_get_user import private_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.private_http_builder import AuthenticationUserModel
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from models.authentication_model import LoginRequestModel, LoginResponseModel
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import (
    assert_create_user_response,
    assert_login_user_response,
)


@pytest.mark.authentication
@pytest.mark.regression
def test_authentication_user():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)
    user_email = response.json().get("user").get("email")
    user_password = request.password
    print(user_email)
    print(user_password)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())

    request = LoginRequestModel(email=user_email, password=user_password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseModel.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
