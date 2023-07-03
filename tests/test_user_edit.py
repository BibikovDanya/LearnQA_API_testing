import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post(f"{default_url}/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post(f"{default_url}/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = requests.put(f"{default_url}/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = requests.get(f"{default_url}/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
        print(response4.content)

    def test_edit_just_created_user_not_auth(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post(f"{default_url}/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed Name"

        response2 = requests.put(f"{default_url}/user/{user_id}",
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_code_status(response2, 400)
        auth_token_not_supplied_message = 'Auth token not supplied'
        assert response2.content.decode('utf-8') == auth_token_not_supplied_message, \
            f"Expected response content: {auth_token_not_supplied_message}. Actual: {response2.content.decode('utf-8')}"

    # TODO разобраться с тестом
    def test_edit_just_created_user_by_other_authorization_user(self):
    #     # REGISTER USER1
    #     register_data_user1 = self.prepare_registration_data()
    #     response_register_user1 = requests.post(f"{default_url}/user", data=register_data_user1)
    #
    #     Assertions.assert_code_status(response_register_user1, 200)
    #     Assertions.assert_json_has_key(response_register_user1, "id")
    #
    #     email_user1 = register_data_user1['email']
    #     first_name_user1 = register_data_user1['firstName']
    #     password_user1 = register_data_user1['password']
    #     user1_id = self.get_json_value(response_register_user1, "id")
    #
    #     # REGISTER USER2
    #     register_data_user2 = self.prepare_registration_data()
    #     response_register_user2 = requests.post(f"{default_url}/user", data=register_data_user2)
    #
    #     Assertions.assert_code_status(response_register_user2, 200)
    #     Assertions.assert_json_has_key(response_register_user2, "id")
    #
    #     email_user2 = register_data_user2['email']
    #     first_name_user2 = register_data_user2['firstName']
    #     password_user2 = register_data_user2['password']
    #     user2_id = self.get_json_value(response_register_user2, "id")
    #
    #     # LOGIN FOR USER2
    #     login_data_user2 = {
    #         'email': email_user2,
    #         'password': password_user2
    #     }
    #     response_login_user2 = requests.post(f"{default_url}/user/login", data=login_data_user2)
    #
    #     auth_sid_user2 = self.get_cookie(response_login_user2, "auth_sid")
    #     token_user2 = self.get_header(response_login_user2, "x-csrf-token")
    #
    #     # EDITING USER DATA USER1 WITH USER AUTHORIZATION USER2
    #     new_name = "Changed Name"
    #
    #     response_editing_data_user1 = requests.put(f"{default_url}/user/{user1_id}",
    #                                                headers={"x-csrf-token": token_user2},
    #                                                cookies={"auth_sid": auth_sid_user2},
    #                                                data={"firstName": new_name}
    #                                                )
    #     Assertions.assert_code_status(response_editing_data_user1, 200)
    #     auth_token_not_supplied_message = 'Auth token not supplied'
    #     assert response_editing_data_user1.content.decode('utf-8') == auth_token_not_supplied_message, \
    #         f"Expected response content: {auth_token_not_supplied_message}. Actual: {response_editing_data_user1.content.decode('utf-8')}"
