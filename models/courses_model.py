from pydantic import BaseModel, Field, ConfigDict

from models.files_model import FileModel
from models.users_model import UserModel


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

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


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

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
