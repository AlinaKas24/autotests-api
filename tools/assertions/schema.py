from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from tools.logger import get_logger

logger = get_logger("SHEMA_ASSERTIONS")


@allure.step("Validate JSON shema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    logger.info("Validate JSON shema")
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
