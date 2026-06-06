from pydantic import BaseModel, Field

from tools.fakers import fake


class TokenModel(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestModel(BaseModel):
    email: str = Field(default_factory=fake.email())
    password: str = Field(default_factory=fake.password())


class RefreshRequestModel(BaseModel):
    refresh_token: str


class LoginResponseModel(BaseModel):
    token: TokenModel
