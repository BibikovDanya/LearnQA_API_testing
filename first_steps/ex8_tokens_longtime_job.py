import requests
import time
from environment import default_url

api_path = 'longtime_job'

def test_adding_task():
    response_add_task = requests.get(f"{default_url}/longtime_job")
    token = response_add_task.json()["token"]
    seconds_to_completion = response_add_task.json()["seconds"]

    assert token != []
    assert seconds_to_completion != []

    response_not_ready_task = requests.get(f"{default_url}/longtime_job", params=f"token={token}")
    assert response_not_ready_task.json()['status'] == "Job is NOT ready"

    time.sleep(seconds_to_completion)
    response_ready_task = requests.get(f"{default_url}/longtime_job", params=f"token={token}")
    assert response_ready_task.json()['status'] == "Job is ready"
    assert response_ready_task.json()['result'] != []
    print(response_ready_task.text)

    response_no_job_linked = requests.get(f"{default_url}/longtime_job", params="token=123")
    assert response_no_job_linked.json()['error'] == "No job linked to this token"
    print(response_no_job_linked.text)