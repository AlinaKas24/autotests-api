from config import settings


def create_allure_environment_file():
    items = []

    for key, value in settings.model_dump().items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                items.append(f"{key}.{sub_key}={sub_value}")
        else:
            items.append(f"{key}={value}")

    properties = "\n".join(items)

    with open(
        settings.allure_results_dir / "environment.properties",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(properties)
