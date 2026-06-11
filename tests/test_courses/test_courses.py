from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture
from models.courses_model import (
    CreateCourseRequestModel,
    GetCoursesQueryModel,
    UpdateCourseRequestModel,
    UpdateCourseResponseModel,
    GetCoursesResponseModel,
)
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_get_courses_response


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_courses(
        self, courses_client: CoursesClient, function_courses: CoursesFixture
    ):
        request = UpdateCourseRequestModel()
        response = courses_client.update_course_api(
            function_courses.response.course.id, request
        )
        response_data = UpdateCourseResponseModel.model_validate_json(response.text)
        print(response_data)

    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_courses: CoursesFixture,
    ):
        query = GetCoursesQueryModel(userId=function_user.response.user.id)
        response = courses_client.get_courses_api(query=query)
        response_data = GetCoursesResponseModel.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_courses.response])
        print(response_data)

    def test_delete_courses(
        self, courses_client: CoursesClient, function_courses: CoursesFixture
    ):
        request = UpdateCourseRequestModel()
        response = courses_client.update_course_api(
            function_courses.response.course.id, request
        )
        course_id = response.json().get("course").get("id")
        response_data = UpdateCourseResponseModel.model_validate_json(response.text)
        response_delete = courses_client.delete_course_api(course_id=course_id)
        response_get = courses_client.get_course_api(course_id=course_id)
        print(response_get.status_code)
