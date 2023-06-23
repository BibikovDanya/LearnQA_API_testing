import pytest
import requests
from environment import default_url
from lib.base_case import BaseCase


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        url = f"{default_url}/user/login"
        response1 = requests.post(url, data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_user_auth(self):

        url = f"{default_url}/user/auth"
        response2 = requests.get(
            url,
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}

        )

        assert "user_id" in response2.json(), "There is not user_id in the second response"

        user_id_from_check_method = response2.json()['user_id']
        assert self.user_id_from_auth_method == user_id_from_check_method, \
            "User id from auth method is not equal to user id from check method "

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        url = f"{default_url}/user/auth"

        if condition == "no_cookie":
            response2 = requests.get(
                url,
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                url,
                cookies={"auth_sid": self.auth_sid}
            )
        assert "user_id" in response2.json(), "There is no user id in second response"

        user_id_from_check_method = response2.json()['user_id']

        assert user_id_from_check_method == 0, f"User is authorized witch condition: {condition}"
