import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url


class TestUserRegister(BaseCase):
    exclude_params = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_uncorrected_email(self):
        uncorrected_email = self.create_email(correct=False)  # email без @
        data = self.prepare_registration_data(uncorrected_email)

        response = requests.post(f"{default_url}/user", data=data)

        Assertions.assert_code_status(response, 400)
        invalid_email_format_message = 'Invalid email format'
        assert response.content.decode('utf-8') == invalid_email_format_message, \
            f"Expected response content: {invalid_email_format_message}. Actual: {response.content.decode('utf-8')}"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_with_missing_required_field(self, condition):
        email = self.create_email()
        match condition:
            case "password":
                data = {
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa',
                    'email': email

                }
            case "username":
                data = {
                    'password': '1234',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa',
                    'email': email
                }
            case "firstName":
                data = {
                    'password': '1234',
                    'username': 'learnqa',
                    'lastName': 'learnqa',
                    'email': email
                }
            case "lastName":
                data = {
                    'password': '1234',
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'email': email
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
        Assertions.assert_code_status(response, 400)

    def test_too_short_name(self):
        name = 'n'
        data = {
            'password': '1234',
            'username': name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.create_email()
        }

        response = requests.post(f"{default_url}/user", data=data)

        short_name_message = f"The value of 'username' field is too short"
        assert response.content.decode('utf-8') == short_name_message, \
            f"Expected response content: {short_name_message}. Actual: {response.content.decode('utf-8')}"

        Assertions.assert_code_status(response, 400)

    def test_too_long_name(self):
        name = 'n' * 251
        data = {
            'password': '1234',
            'username': name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.create_email()
        }

        response = requests.post(f"{default_url}/user", data=data)

        short_name_message = f"The value of 'username' field is too long"
        assert response.content.decode('utf-8') == short_name_message, \
            f"Expected response content: {short_name_message}. Actual: {response.content.decode('utf-8')}"

        Assertions.assert_code_status(response, 400)
