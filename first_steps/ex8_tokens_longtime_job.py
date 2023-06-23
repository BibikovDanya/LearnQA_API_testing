import requests
import time
from environment import default_url

api_path = 'longtime_job'


def test_adding_task():
    response_add_task = requests.get(f"{default_url}/longtime_job")
    assert response_add_task.status_code == 200, f"Wrong status code: {response_add_task.status_code}"
    response_dict_add_task = response_add_task.json()

    assert "token" in response_dict_add_task, "There is not field 'token' in the response"
    assert "seconds" in response_dict_add_task, "There is not field 'seconds' in the response"
    token = response_dict_add_task["token"]
    seconds_to_completion = response_dict_add_task["seconds"]

    response_not_ready_task = requests.get(f"{default_url}/longtime_job", params=f"token={token}")
    response_not_ready_task_dict = response_not_ready_task.json()
    assert 'status' in response_not_ready_task_dict
    assert response_not_ready_task_dict['status'] == "Job is NOT ready"

    time.sleep(seconds_to_completion)
    response_ready_task = requests.get(f"{default_url}/longtime_job", params=f"token={token}")
    response_ready_task_dict = response_ready_task.json()
    assert 'status' in response_ready_task_dict, "There is not field 'status' in the response"
    assert 'result' in response_ready_task_dict, "There is not field 'result' in the response"

    assert response_ready_task_dict['status'] == "Job is ready",\
        f"Wrong status, expected: {response_ready_task_dict['status']}"
    assert response_ready_task_dict['result'] != [],\
        f"Wrong result, expected: {response_ready_task_dict['result']}"

    response_no_job_linked = requests.get(f"{default_url}/longtime_job", params="token=123")
    response_no_job_linked_dict = response_no_job_linked.json()
    assert 'error' in response_no_job_linked_dict, "There is not field 'error' in the response"
    assert response_no_job_linked_dict['error'] == "No job linked to this token", \
        f"Wrong status, expected: {response_no_job_linked_dict['error']}"
