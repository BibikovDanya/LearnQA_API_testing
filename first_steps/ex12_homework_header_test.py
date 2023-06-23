import requests
from environment import default_url
from lib.base_case import BaseCase


def test_homework_header():
    base_case = BaseCase()
    response = requests.get(f"{default_url}/homework_header")
    assert response.status_code == 200, f"Received the status code is not 200 but {response.status_code}"

    actual_value_headers = base_case.get_header(response, 'x-secret-homework-header')
    expect_value_headers = 'Some secret value'
    assert actual_value_headers == expect_value_headers, \
        f"Actual value cookie is '{actual_value_headers}', expected is '{expect_value_headers}'"
