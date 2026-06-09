from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


class FileModel(BaseModel):
    """
    Описание структуры файла.
    """

    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestModel(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseModel(BaseModel):
    """
    Описание структуры ответа создания файла.
    """

    file: FileModel


class GetFileResponseModel(BaseModel):
    file: FileModel
