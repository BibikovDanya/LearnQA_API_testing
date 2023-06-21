import requests
from environment import default_url

response = requests.get(f'{default_url}/get_text')
print(response.text)