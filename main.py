import requests


def test_test_one():
    """
    :return: response text
    """
    response = requests.get('https://playground.learnqa.ru/api/hello')
    return response.text


def main():
    test_test_one()


if __name__ == '__main__':
    main()
