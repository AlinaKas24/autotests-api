from models.courses_model import (
    CourseModel,
    GetCoursesResponseModel,
    CreateCourseResponseModel,
    UpdateCourseRequestModel,
    UpdateCourseResponseModel,
)
from tools.assertions.base import assert_equal, assert_length


def assert_update_course_response(
    request: UpdateCourseRequestModel, response: UpdateCourseResponseModel
):
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.maxScore, request.max_score, "max_score")
    assert_equal(response.course.minScore, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(
        response.course.estimated_time, request.estimated_time, "estimated_time"
    )


def assert_course(actual: CourseModel, expected: CourseModel):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_courses_response(
    get_courses_response: GetCoursesResponseModel,
    create_course_responses: list[CreateCourseResponseModel],
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(
            get_courses_response.courses[index], create_course_response.course
        )
