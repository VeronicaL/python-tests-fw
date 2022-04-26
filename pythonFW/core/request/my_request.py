import requests
from environment import ENV
from utils.logger import Logger


class Request:

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None):
        return Request._send(url, data, headers, 'GET')

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None):
        return Request._send(url, data, headers, 'POST')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, method: str):
        url = f"{ENV.base_url()}{url}"
        if headers is None:
            headers = {}

        Logger.get_instance().add_request(url, data, headers, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers)
        else:
            raise Exception(f'Unsupported HTTP method "{method}" was called')

        Logger.get_instance().add_response(response)
        return response
