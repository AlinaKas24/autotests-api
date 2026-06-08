from http import HTTPStatus
import pytest
from clients.private_http_builder import AuthenticationUserModel
from conftest import UserFixture
from models.authentication_model import LoginRequestModel, LoginResponseModel
from tools.assertions.base import assert_status_code


@pytest.mark.authentication
@pytest.mark.regression
def test_authentication_user(
    authentication_client: AuthenticationUserModel, function_user: UserFixture
):
    login_request = LoginRequestModel(
        email=function_user.email, password=function_user.password
    )
    print(function_user.email)
    print(function_user.password)

    response = authentication_client.login_api(login_request)
    response_data = LoginResponseModel.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
