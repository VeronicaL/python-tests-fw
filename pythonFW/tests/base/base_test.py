from requests import Response
from datetime import datetime
from utils.logger import Logger


class BaseTest:

    _headers = {'Content-type': 'application/json'}

    def setup(self):
        pass

    def teardown(self):
        Logger.get_instance().write_log_to_file()


    @staticmethod
    def create_unique_email(base: str, domain="gmail.com"):
        return f'{base} + {datetime.now().strftime("%m%d%Y%H%M%S")}@{domain}'

