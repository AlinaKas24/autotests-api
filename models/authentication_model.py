from pydantic import BaseModel, Field


class TokenModel(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestModel(BaseModel):
    email: str
    password: str


class RefreshRequestModel(BaseModel):
    refresh_token: str


class LoginResponseModel(BaseModel):
    token: TokenModel
