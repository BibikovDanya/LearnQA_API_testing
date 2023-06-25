import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url


class TestUserRegister(BaseCase):
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

        assert response.status_code == 400, f"Received the status code is not 400 but {response.status_code}"
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"
