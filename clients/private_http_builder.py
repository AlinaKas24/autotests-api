from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import (
    get_authentication_client,
)
from models.authentication_model import LoginRequestModel


class AuthenticationUserModel(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserModel) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestModel(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)
    return Client(
        timeout=10,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
    )
