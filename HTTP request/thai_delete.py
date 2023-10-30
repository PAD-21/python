import requests

response = requests.delete("https://httpbin.org/delete")

print(response.status_code)

print(response.text)