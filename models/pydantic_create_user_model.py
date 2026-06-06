from pydantic import BaseModel, EmailStr, Field

from tools.fakers import fake


class CreateUserRequestSchema(BaseModel):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.first_name)


class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
