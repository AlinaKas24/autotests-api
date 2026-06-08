import pytest
from clients.users.private_users_client import PrivateUsersClient
from conftest import UserFixture
from models.users_model import GetUserResponseModel


@pytest.mark.authentication
@pytest.mark.regression
def test_authentication_user(
    function_user: UserFixture,
    private_user_client: PrivateUsersClient,
):
    response = private_user_client.get_user_me_api()
    print(response.json())
    GetUserResponseModel.model_validate_json(response.text)
