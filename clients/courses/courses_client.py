from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient


class GetCoursesRequestDict(TypedDict):
    userId: str


class CreateCoursesRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCoursesRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesRequestDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"/api/v1/courses", params=query)

    def create_courses_api(self, request: CreateCoursesRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/courses", json=request)

    def get_courses_by_id_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_courses_by_id_api(
        self, course_id: str, request: UpdateCoursesRequestDict
    ) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_courses_by_id_api(
        self,
        course_id: str,
    ) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.delete(f"/api/v1/courses/{course_id}")
