import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    #
    # logger.debug("Message DEBUG level")
    # logger.info("Message INFO level")
    # logger.warning("Message WARNING level")
    # logger.error("Message ERROR level")
    # logger.critical("Message CRITICAL level")
    return logger
