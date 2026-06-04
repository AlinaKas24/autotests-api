from pydantic import BaseModel, HttpUrl


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

    filename: str
    directory: str
    upload_file: str


class CreateFileResponseModel(BaseModel):
    """
    Описание структуры ответа создания файла.
    """

    file: FileModel
