import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.expected_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email

        }

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.expected_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

