from pydantic import BaseModel, Field, ConfigDict

from models.files_model import FileModel
from models.users_model import UserModel
from tools.fakers import fake


class CourseModel(BaseModel):
    """
    Описание структуры курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileModel = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserModel = Field(alias="createdByUser")


class GetCoursesResponseModel(BaseModel):
    """
    Описание структуры ответа на получение списка курсов.
    """

    courses: list[CourseModel]


class GetCoursesQueryModel(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """

    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseRequestModel(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.text)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.description)
    estimated_time: str = Field(
        alias="estimatedTime", default_factory=fake.estimate_time
    )
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class CreateCourseResponseModel(BaseModel):
    """
    Описание структуры ответа создания курса.
    """

    course: CourseModel


class UpdateCourseRequestModel(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.text)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.description)
    estimated_time: str | None = Field(
        alias="estimatedTime", default_factory=fake.estimate_time
    )


class UpdateCourseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    maxScore: int = Field(alias="maxScore")
    minScore: int = Field(alias="minScore")
    description: str
    preview_file: FileModel = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserModel = Field(alias="createdByUser")


class UpdateCourseResponseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    course: UpdateCourseModel
