from http import HTTPStatus

import pytest

from clients.errors_model import NotFoundErrorResponseModel
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExercisesFixture
from models.exercise_model import (
    CreateExerciseRequestModel,
    CreateExerciseResponseModel,
    GetExerciseResponseModel,
    UpdateExerciseRequestModel,
    UpdateExerciseResponseModel,
    GetExercisesQueryModel,
    GetExercisesResponseModel,
)
from tools.assertions.base import assert_status_code
from tools.assertions.exercise import (
    assert_create_exercise_response,
    assert_get_exercise_response,
    assert_update_exercise_response,
    assert_delete_exercise_not_found_response,
    assert_get_exercises_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self, exercises_client: ExercisesClient, function_courses: CoursesFixture
    ):
        request = CreateExerciseRequestModel(
            courseId=function_courses.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_exercise_response(request, response_data)

    def test_get_exercise(
        self, exercises_client: ExercisesClient, function_exercises: ExercisesFixture
    ):
        response = exercises_client.get_exercise_api(
            exercise_id=function_exercises.response.exercise.id
        )
        response_data = GetExerciseResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercises.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
        self, exercises_client: ExercisesClient, function_exercises: ExercisesFixture
    ):
        request = UpdateExerciseRequestModel()
        response = exercises_client.update_exercise_api(
            function_exercises.response.exercise.id, request
        )
        response_data = UpdateExerciseResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(
        self, exercises_client: ExercisesClient, function_exercises: ExercisesFixture
    ):
        exercise_id = function_exercises.response.exercise.id
        response = exercises_client.delete_exercise_api(exercise_id=exercise_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_get = exercises_client.get_exercise_api(exercise_id=exercise_id)
        response_data = NotFoundErrorResponseModel.model_validate_json(
            response_get.text
        )
        assert_status_code(response_get.status_code, HTTPStatus.NOT_FOUND)
        assert_delete_exercise_not_found_response(response_data)
        validate_json_schema(response_get.json(), response_data.model_json_schema())

    def test_get_exercises(
        self,
        exercises_client: ExercisesClient,
        function_exercises: ExercisesFixture,
        function_courses: CoursesFixture,
    ):
        query = GetExercisesQueryModel(courseId=function_courses.response.course.id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercises.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
