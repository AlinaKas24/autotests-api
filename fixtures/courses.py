import pytest

from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from models.courses_model import CreateCourseRequestModel, CreateCourseResponseModel


class CoursesFixture(BaseModel):
    request: CreateCourseRequestModel
    response: CreateCourseResponseModel


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_courses(
    courses_client: CoursesClient,
    function_user: UserFixture,
    function_files: FileFixture,
) -> CoursesFixture:
    request = CreateCourseRequestModel(
        previewFileId=function_files.response.file.id,
        createdByUserId=function_user.response.user.id,
    )
    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)
