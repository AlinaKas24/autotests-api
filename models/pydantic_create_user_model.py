from pydantic import BaseModel, EmailStr


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    lastName: str
    firstName: str
    middleName: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
