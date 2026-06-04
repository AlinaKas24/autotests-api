from pydantic import BaseModel, EmailStr, Field


class CreateUserRequestSchema(BaseModel):
    email: str
    password: str
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
