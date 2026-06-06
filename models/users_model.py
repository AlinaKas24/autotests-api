from pydantic import BaseModel, Field

from tools.fakers import fake


class UserModel(BaseModel):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


# Добавили описание структуры ответа получения пользователя
class GetUserResponseModel(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """

    user: UserModel


class UpdateUserRequestModel(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """

    email: str | None
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name())
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name())
    middle_name: str | None = Field(
        alias="middleName", default_factory=fake.middle_name()
    )
