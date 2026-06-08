import pytest
from pydantic import BaseModel
from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.files.files_client import FilesClient, get_files_client
from fixtures.courses import function_courses, CoursesFixture
from fixtures.users import UserFixture
from models.exercise_model import (
    CreateExerciseRequestModel,
    CreateExerciseResponseModel,
)

class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestModel
    response: CreateExerciseResponseModel


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercises(
    exercises_client: ExercisesClient,function_courses:CoursesFixture
) -> ExercisesFixture:
    request = CreateExerciseRequestModel(courseId=function_courses.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)
