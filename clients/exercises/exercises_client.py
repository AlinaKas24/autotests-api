from httpx import Response

from clients.api_client import ApiClient
from clients.private_http_builder import (
    AuthenticationUserModel,
    get_private_http_client,
)
from models.exercise_model import (
    GetExercisesQueryModel,
    CreateExerciseRequestModel,
    UpdateExerciseRequestModel,
    GetExercisesResponseModel,
    GetExerciseResponseModel,
    UpdateExerciseResponseModel,
    CreateExerciseResponseModel,
)
from tools.routes import APIRoutes


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryModel) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(
            f"{APIRoutes.EXERCISES}", params=query.model_dump(by_alias=True)
        )

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestModel) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            f"{APIRoutes.EXERCISES}", json=request.model_dump(by_alias=True)
        )

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestModel
    ) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"{APIRoutes.EXERCISES}/{exercise_id}",
            json=request.model_dump(by_alias=True),
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryModel) -> GetExercisesResponseModel:
        response = self.get_exercises_api(query)
        return GetExercisesResponseModel.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseModel:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseModel.model_validate_json(response.text)

    def create_exercise(
        self, request: CreateExerciseRequestModel
    ) -> CreateExerciseResponseModel:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseModel.model_validate_json(response.text)

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestModel
    ) -> UpdateExerciseResponseModel:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseModel.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserModel) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
