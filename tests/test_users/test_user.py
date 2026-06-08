from http import HTTPStatus

import pytest

from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake


@pytest.mark.parametrize(
    "email",
    ["mail.ru", "gmail.com", "example.com"],
)
@pytest.mark.users
@pytest.mark.regression
class TestUsersMe:
    def test_create_user(self, public_user_client: PublicUsersClient, email):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        # print(request)
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
