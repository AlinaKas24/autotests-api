import allure

from clients.errors_model import (
    ValidationErrorModel,
    ValidationErrorResponseModel,
    NotFoundErrorResponseModel,
    IncorrectFileIdErrorResponseModel,
    IncorrectFileIdErrorModel,
)
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("ERRORS_ASSERTIONS")  # Создаем логгер с именем "ERRORS_ASSERTIONS"


@allure.step("Check validation error")
def assert_validation_errors(
    actual: ValidationErrorModel, expected: ValidationErrorModel
):
    logger.info("Check validation error")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.type, expected.type, "input")
    assert_equal(actual.type, expected.type, "contex")
    assert_equal(actual.type, expected.type, "message")
    assert_equal(actual.type, expected.type, "location")


@allure.step("Check validation error response")
def assert_validation_errors_response(
    actual: ValidationErrorResponseModel, expected: ValidationErrorResponseModel
):
    # Логируем факт начала проверки
    logger.info("Check validation error response")
    assert_length(actual.details, expected.details, "details")
    for index, detail in enumerate(expected.details):
        assert_validation_errors(actual.details[index], detail)


def assert_not_found_errors_response(
    actual: NotFoundErrorResponseModel, expected: NotFoundErrorResponseModel
):
    assert_equal(actual.details, expected.details, "details")


def assert_incorrect_file_id_errors(
    actual: IncorrectFileIdErrorModel, expected: IncorrectFileIdErrorModel
):
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.type, expected.type, "loc")
    assert_equal(actual.type, expected.type, "msg")
    assert_equal(actual.type, expected.type, "input")
    assert_equal(actual.type, expected.type, "ctx")


def assert_incorrect_file_id_errors_response(
    actual: IncorrectFileIdErrorResponseModel,
    expected: IncorrectFileIdErrorResponseModel,
):
    assert_length(actual.details, expected.details, "detail")
    for index, detail in enumerate(expected.details):
        assert_incorrect_file_id_errors(actual.details[index], detail)
