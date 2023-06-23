import pytest
import requests
from environment import default_url


class TestFirstApi:
    names = [
        ("Alex"),
        ("Kim"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = f"{default_url}/hello"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, f"Wrong response status code, expected: {response.status_code}"

        response_dict = response.json()
        assert "answer" in response_dict, f"There is not 'answer' in the response"

        if len(name) == 0:
            expected_response_text = f"Hello, someone"

        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, f"Actual text in the response is not correct"
