import jsonschema

from clients.users.public_users_client import get_public_users_client
from models.pydantic_create_user_model import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(
    instance=create_user_response.json(), schema=create_user_response_schema
)
