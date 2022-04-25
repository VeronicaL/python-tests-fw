import allure
from core.my_request import Request
from core.base_test import BaseTest
from core.asserts import Asserts


@allure.epic("Check users info")
class TestUsersInfo(BaseTest):

    @allure.description("This test checks if here are any people in the library")
    def test_get_users(self):
        response = Request.get('users')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_has_header(response, "Transfer-Encoding")
        Asserts.assert_not_empty(response.json(), "There are no users in the library.")




