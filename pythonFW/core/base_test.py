from requests import Response
from datetime import datetime
from core.logger import Logger


class BaseTest:

    _headers = {'Content-type': 'application/json'}

    def setup(self):
        pass

    def teardown(self):
        Logger.get_instance().write_log_to_file()

    @staticmethod
    def get_header(response: Response, header_name):
        if header_name in response.headers:
            return {header_name: response.headers[header_name]}
        else:
            raise Exception(f"Cannot find header with the name {header_name} in the last response")

    @staticmethod
    def create_unique_email(base: str, domain="gmail.com"):
        return f'{base} + {datetime.now().strftime("%m%d%Y%H%M%S")}@{domain}'

