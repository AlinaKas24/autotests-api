import allure

from clients.errors_model import NotFoundErrorResponseModel
from models.exercise_model import (
    CreateExerciseRequestModel,
    CreateExerciseResponseModel,
    ExerciseModel,
    GetExerciseResponseModel,
    UpdateExerciseRequestModel,
    UpdateExerciseResponseModel,
    GetExercisesResponseModel,
)
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_not_found_errors_response

from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check create exercise response")
def assert_create_exercise_response(
    request: CreateExerciseRequestModel, response: CreateExerciseResponseModel
):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(
        response.exercise.estimated_time, request.estimated_time, "estimated_time"
    )


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseModel, expected: ExerciseModel):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(
    get_exercise_response: GetExerciseResponseModel,
    create_exercise_responses: CreateExerciseResponseModel,
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответам на их создание.

    :param get_exercise_response: Ответ API при запросе упражнения.
    :param create_exercise_responses: Список API ответов при созданииупражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """
    logger.info("Check get exercise response")
    assert_exercise(get_exercise_response.exercise, create_exercise_responses.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
    request: UpdateExerciseRequestModel, response: UpdateExerciseResponseModel
):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(
        response.exercise.estimated_time, request.estimated_time, "estimated_time"
    )


@allure.step("Check exercise not found response")
def assert_delete_exercise_not_found_response(
    actual: NotFoundErrorResponseModel,
):
    logger.info("Check exercise not found response")
    expected = NotFoundErrorResponseModel(detail="Exercise not found")
    assert_not_found_errors_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseModel,
    create_exercise_responses: list[CreateExerciseResponseModel],
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка курсов.
    :param create_exercise_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    logger.info("Check get exercises response")
    assert_length(
        get_exercises_response.exercises, create_exercise_responses, "exercises"
    )

    for index, create_exercise_responses in enumerate(create_exercise_responses):
        assert_exercise(
            get_exercises_response.exercises[index], create_exercise_responses.exercise
        )
