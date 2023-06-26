import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url
from datetime import datetime


class TestUserRegister(BaseCase):
    exclude_params = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]

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

    def test_create_user_with_uncorrected_email(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        uncorrected_email = f"{base_part}{random_part}{domain}"  # email без @
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': uncorrected_email

        }

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.expected_status_code(response, 400)
        invalid_email_format_message = 'Invalid email format'
        assert response.content.decode('utf-8') == invalid_email_format_message, \
            f"Expected response content: {invalid_email_format_message}. Actual: {response.content.decode('utf-8')}"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_with_missing_required_field(self, condition):
        match condition:
            case "password":
                data = {
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa',
                    'email': self.email

                }
            case "username":
                data = {
                    'password': '1234',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa',
                    'email': self.email
                }
            case "firstName":
                data = {
                    'password': '1234',
                    'username': 'learnqa',
                    'lastName': 'learnqa',
                    'email': self.email
                }
            case "lastName":
                data = {
                    'password': '1234',
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'email': self.email
                }
            case "email":
                data = {
                    'password': '1234',
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa'
                }

        response = requests.post(f"{default_url}/user", data=data)

        missing_required_field_message = f"The following required params are missed: {condition}"
        assert response.content.decode('utf-8') == missing_required_field_message, \
            f"Expected response content: {missing_required_field_message}. Actual: {response.content.decode('utf-8')}"
        Assertions.expected_status_code(response, 400)

