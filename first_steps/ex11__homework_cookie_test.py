import requests
from environment import default_url
from lib.base_case import BaseCase


def test_homework_cookie():
    base_case = BaseCase()
    response = requests.get(f"{default_url}/homework_cookie")
    assert response.status_code == 200, f"Received the status code is not 200 but {response.status_code}"

    actual_value_cookie = base_case.get_cookie(response, "HomeWork")
    expect_value_cookie = 'hw_value'
    assert actual_value_cookie == expect_value_cookie, \
        f"Actual value cookie is '{actual_value_cookie}', expected is '{expect_value_cookie}'"
