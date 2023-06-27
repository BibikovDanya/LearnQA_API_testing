import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from environment import default_url


class TestUserGet(BaseCase):
    def test_user_get_details_not_auth(self):
        response = requests.get(f"{default_url}/user/2")
        print(response.content)

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")
