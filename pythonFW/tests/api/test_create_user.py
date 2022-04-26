import json

import allure
import pytest
from tests.base.base_test import BaseTest
from core.request.my_request import Request
from utils.asserts import Asserts
from model.user import User


@allure.epic("Create user cases")
class TestCreateUser(BaseTest):
    users_provider = [
        ("Katja", "Ivanova", "tyue@mail.ru"),
        ("Marina", "Denisenko", "tplujk@mail.ru"),
        ("Alina", "Polinkasd", "ddssaa@mail.ru")
    ]

    @allure.description("This test checks several users creation with required fields")
    @pytest.mark.parametrize('name,secondName,email', users_provider)
    def test_create_users_from_provider(self, name: str, secondName: str, email: str):
        response = Request.post("user", json.dumps(User.userinfo(name, secondName, email)), self._headers)

        Asserts.assert_code_status(response, 200)

    @allure.description("This test is trying to create user without secondName")
    def test_not_enough_data(self):
        data = {
            "name": "Veronica",
            "email": "rrr@asd.com",
        }

        response = Request.post("user", data, self._headers)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_text_in_response(response, "Bad Request")

    @allure.description("This test checks user creation with required fields")
    def test_create_user_successfully(self):
        new_user = {
            "name": "Nikita",
            "secondName": "Lapunka",
            "email": self.create_unique_email('test'),
        }

        response = Request.post("user", json.dumps(new_user), self._headers)
        Asserts.assert_code_status(response, 200)






