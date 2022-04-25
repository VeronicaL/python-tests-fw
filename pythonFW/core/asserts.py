from requests import Response


class Asserts:

    @staticmethod
    def assert_equals(val1, val2, error_message: str = ""):
        assert val1 == val2, f"Assertion failed: {val1} is not equal {val2}. {error_message}"

    @staticmethod
    def assert_not_empty(json, error_message: str = ""):
        assert len(json) > 0, f"Assertion failed. {error_message}"

    @staticmethod
    def assert_code_status(response: Response, expected_code: int, message: str = ""):
        assert response.status_code == expected_code, \
            f"Expected status code is {expected_code}, but we got {response.status_code}. {message}"

    @staticmethod
    def assert_response_text(response: Response, expected_text: str, message: str = ""):
        assert response.text == expected_text, \
            f'Expected response text is "{expected_text}", but we got "{response.text}". {message}'

    @staticmethod
    def assert_text_in_response(response: Response, text: str, message: str = ""):
        assert text in response.text, \
            f'Text "{text}" is not in the response, we got "{response.text}". {message}'

    @staticmethod
    def assert_response_has_header(response: Response, key: str):
        assert key in response.headers, \
            f"Cannot find header with the name {key} in the response. All headers in the response: " \
            + str(response.headers)
