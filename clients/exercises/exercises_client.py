from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient


class GetExerciseRequestDict(TypedDict):
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExerciseRequestDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/exercises", json=request)

    def get_exercises_by_id_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_by_id_api(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title,maxScore,minScore,orderIndex,description,estimatedTime..
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_by_id_api(
        self,
        exercise_id: str,
    ) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.delete(f"/api/v1/exercises/{exercise_id}")
