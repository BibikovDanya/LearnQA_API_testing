import requests
from environment import default_url

response = requests.get(f"{default_url}/long_redirect", allow_redirects=True)
history = response.history
print(len(history))
print(str(response.url))