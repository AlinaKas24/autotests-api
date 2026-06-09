from clients.errors_model import (
    ValidationErrorResponseModel,
    ValidationErrorModel,
    NotFoundErrorResponseModel,
)
from tools.assertions.errors import (
    assert_validation_errors_response,
    assert_not_found_errors_response,
)


def assert_create_file_with_empy_file_name_response(
    actual: ValidationErrorResponseModel,
):
    expected = ValidationErrorResponseModel(
        details=[
            ValidationErrorModel(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"],
            )
        ]
    )
    assert_validation_errors_response(actual, expected)


def assert_create_file_with_empy_directory_response(
    actual: ValidationErrorResponseModel,
):
    expected = ValidationErrorResponseModel(
        detail=[
            ValidationErrorModel(
                type="string_too_short",
                input="",
                ctx={"min_length": 1},
                msg="String should have at least 1 character",
                loc=["body", "directory"],
            )
        ]
    )
    assert_validation_errors_response(actual, expected)


def assert_delete_file_not_found_response(
    actual: NotFoundErrorResponseModel,
):
    expected = NotFoundErrorResponseModel(detail="File not found")
    assert_not_found_errors_response(actual, expected)
