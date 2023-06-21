import requests
import json
from json.decoder import JSONDecodeError

default_url = 'https://playground.learnqa.ru/api'


# Home work 1 lesson 1
def test_get_text():
    response = requests.get(f"{default_url}/get_text")
    expect_result = '<Response [200]>'
    response = str(response)
    assert response == expect_result


