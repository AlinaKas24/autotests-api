from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    details: list[ValidationErrorModel] = Field(alias="detail")


class NotFoundErrorResponseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    details: str = Field(alias="detail")


class IncorrectFileIdErrorModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str
    loc: list[str]
    message: str = Field(alias="msg")
    input: str
    context: dict[str, Any] = Field(alias="ctx")


class IncorrectFileIdErrorResponseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    details: list[IncorrectFileIdErrorModel] = Field(alias="detail")
