from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from fixtures.users import UserFixture
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from models.users_model import GetUserResponseModel
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.tag(AllureTag.USERS, AllureTag.USERS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.USERS)  #
class TestUsersMe:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @pytest.mark.parametrize(
        "email",
        ["mail.ru", "gmail.com", "example.com"],
    )
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(self, public_user_client: PublicUsersClient, email):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    @allure.severity(Severity.CRITICAL)
    def test_authentication_user(
        self,
        function_user: UserFixture,
        private_user_client: PrivateUsersClient,
    ):
        response = private_user_client.get_user_me_api()
        print(response.json())
        GetUserResponseModel.model_validate_json(response.text)
