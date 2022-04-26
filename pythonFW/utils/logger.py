import datetime
import allure
import logging
import os
from requests import Response


class Logger:
    instance = None
    path = "logger.log"
    data = ""

    def __init__(self):
        if os.path.exists(self.path):
            os.remove(self.path)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(self.path)
        handler.setLevel(logging.DEBUG)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def clear_data(self):
        self.data = ""

    @allure.step("{method} request to {url}")
    def add_request(self, url: str, data: dict, headers: dict, method: str):
        data_to_add = f"\n-----\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request method: {method}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request URL: {url}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request data: {data}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request headers: {headers}"
        data_to_add += "\n"

        self.data += data_to_add
        self.logger.info(data_to_add)

    def add_response(self, response: Response):
        headers_as_dict = dict(response.headers)

        data_to_add = f"\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response code: {response.status_code}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response text: {response.text}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response headers: {headers_as_dict}"
        data_to_add += "\n-----\n"

        self.data += data_to_add
        self.logger.info(data_to_add)


    def write_log_to_file(self):
        with open(self.path, 'a', encoding='utf-8') as logger_file:
            testname = os.environ.get('PYTEST_CURRENT_TEST')
            logger_file.write(f"START TEST {testname}\n")
            logger_file.write(self.data)
            logger_file.write(f"\nEND TEST {testname}\n\n")
            self.clear_data()


    