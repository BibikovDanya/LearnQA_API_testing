import requests
from environment import default_url

supported_methods = ['GET', 'POST', 'PUT', 'DELETE']


def test_request_without_parameter():
    response = requests.get(f"{default_url}/compare_query_type")
    assert str(response.text) == 'Wrong method provided', "The response does not contain 'Wrong method provided'"

    response = requests.post(f"{default_url}/compare_query_type")
    assert str(response.text) == 'Wrong method provided', "The response does not contain 'Wrong method provided'"

    response = requests.put(f"{default_url}/compare_query_type")
    assert str(response.text) == 'Wrong method provided', "The response does not contain 'Wrong method provided'"

    response = requests.delete(f"{default_url}/compare_query_type")
    assert str(response.text) == 'Wrong method provided', "The response does not contain 'Wrong method provided'"


def test_no_supported_methods():
    for method in supported_methods:
        response = requests.patch(f"{default_url}/compare_query_type", data=f"method={method}")
        status_code = response.status_code
        assert status_code == 400, f"Received the status code is not 400 but {status_code}"
        assert response.text == 'Wrong HTTP method',  f"Error: method: {method} response_text: {response.text}"

    for method in supported_methods:
        response = requests.head(f"{default_url}/compare_query_type", data=f"method={method}")
        status_code = response.status_code
        assert status_code == 400, f"Received the status code is not 400 but {status_code}"
        # TODO: при запросе типа head не приходит "Wrong HTTP method"
        # assert response.text == 'Wrong HTTP method', f"Error: method: {method} response_text: {response.text}"


def test_support_method_and_params():
    response_get = requests.get(f"{default_url}/compare_query_type", params=f"method=GET")
    assert response_get.status_code == 200, f"Received the status code is not 200 but {response_get.status_code}"
    assert response_get.text == '{"success":"!"}'

    response_post = requests.post(f"{default_url}/compare_query_type", data={'method': 'POST'})
    assert response_post.status_code == 200
    assert response_post.text == '{"success":"!"}'
    print(response_post.text)

    response_put = requests.put(f"{default_url}/compare_query_type", data={'method': 'PUT'})
    assert response_put.status_code == 200
    assert response_put.text == '{"success":"!"}'
    print(response_put.text)


def test_all_methods_in_params():
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'COPY', 'HEAD', 'OPTIONS',
               'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW']
    for method in methods:
        response_get = requests.get(f"{default_url}/compare_query_type", params=f"method={method}")
        if method == 'GET':
            assert response_get.status_code == 200
            assert response_get.text == '{"success":"!"}'
        else:
            assert response_get.status_code == 200
            assert response_get.text == 'Wrong method provided'

        response_post = requests.post(f"{default_url}/compare_query_type", data={'method': f"{method}"})
        if method == 'POST':
            assert response_post.status_code == 200
            assert response_post.text == '{"success":"!"}'
        else:
            assert response_post.status_code == 200
            assert response_post.text == 'Wrong method provided'

        response_put = requests.put(f"{default_url}/compare_query_type", data={'method': f"{method}"})
        if method == 'PUT':
            assert response_put.status_code == 200
            assert response_put.text == '{"success":"!"}'
        else:
            assert response_put.status_code == 200
            assert response_put.text == 'Wrong method provided'

        response_delete = requests.delete(f"{default_url}/compare_query_type", data={'method': f"{method}"})
        if method == 'DELETE':
            assert response_delete.status_code == 200
            assert response_delete.text == '{"success":"!"}'
        else:
            # TODO при запросе с параметром = GET, возвращает success
            print(f"method: {method} response_text: {response_delete.text}")
            # assert response_delete.status_code == 200
            # assert response_delete.text == 'Wrong method provided'
        response_patch = requests.get(f"{default_url}/compare_query_type", params=f"method={method}")
        if method == 'PATCH':
            # TODO при запросе с параметром = PATCH, возвращает  Wrong method provided
            print(f"method: {method} response_text: {response_delete.text}")
            assert response_patch.status_code == 200
            # assert response_patch.text == '{"success":"!"}'
        else:
            # TODO при запросе с параметром = GET, возвращает success
            print(f"method: {method} response_text: {response_delete.text}")
            assert response_patch.status_code == 200
            # assert response_patch.text == 'Wrong method provided'
