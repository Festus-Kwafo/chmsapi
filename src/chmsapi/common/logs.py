import json_log_formatter
import os
import logging
from logging.handlers import RotatingFileHandler
from src.chmsapi.config.path_conf import LogPath

from src.chmsapi.config.settings import settings


class Logger:
    def __init__(self):
        self.log_path = LogPath

    def log(self) -> json_log_formatter.JSONFormatter():
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        formatter = json_log_formatter.JSONFormatter()

        log_stdout_file = os.path.join(self.log_path, settings.LOG_STDOUT_FILENAME)

        json_handler = logging.handlers.RotatingFileHandler(filename=log_stdout_file, maxBytes=20000, backupCount=5)

        json_handler.setFormatter(formatter)
        logger = logging.getLogger('my_json')

        if not logger.hasHandlers():
            logger.addHandler(json_handler)
            logger.setLevel(logging.DEBUG)
            return logger


log = Logger().log()
