from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class ExerciseModel(BaseModel):
    """
    Описание структуры задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseModel(BaseModel):
    """
    Описание структуры ответа на получение задания..
    """

    exercise: ExerciseModel


class GetExercisesQueryModel(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """

    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class GetExercisesResponseModel(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """

    exercises: list[ExerciseModel]


class CreateExerciseRequestModel(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.description)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(
        alias="estimatedTime", default_factory=fake.estimate_time
    )


class CreateExerciseResponseModel(BaseModel):
    """
    Описание структуры ответа создания задания.
    """

    exercise: ExerciseModel


class UpdateExerciseRequestModel(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.description)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(
        alias="estimatedTime", default_factory=fake.estimate_time
    )


class UpdateExerciseResponseModel(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """

    exercise: ExerciseModel
