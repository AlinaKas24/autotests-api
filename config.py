from pathlib import Path
from typing import Self

from pydantic import BaseModel, FilePath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl = "http://localhost:8000"
    timeout: float = 100

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath = Path("./testdata/files/image.png")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    test_data: TestDataConfig = TestDataConfig()
    http_client: HTTPClientConfig = HTTPClientConfig()

    # Path вместо DirectoryPath
    allure_results_dir: Path = Path("./allure-results")

    @classmethod
    def initialize(cls) -> Self:
        settings = cls()
        settings.allure_results_dir.mkdir(parents=True, exist_ok=True)
        return settings


settings = Settings.initialize()
