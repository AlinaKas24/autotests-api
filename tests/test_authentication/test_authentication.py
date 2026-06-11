from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.private_http_builder import AuthenticationUserModel
from fixtures.users import UserFixture

from models.authentication_model import LoginRequestModel, LoginResponseModel
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code


@pytest.mark.authentication
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:

    @allure.title("Login user")
    @allure.story(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_authentication_user(
        self, authentication_client: AuthenticationUserModel, function_user: UserFixture
    ):
        login_request = LoginRequestModel(
            email=function_user.email, password=function_user.password
        )
        print(function_user.email)
        print(function_user.password)

        response = authentication_client.login_api(login_request)
        response_data = LoginResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
