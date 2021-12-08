import requests

response = requests.get("https://api.sunrise-sunset.org/json")

print(response.status_code)
print(response.json())