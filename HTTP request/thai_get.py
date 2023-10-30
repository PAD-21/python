import requests

#response = requests.get("https://youtube.com")
response = requests.get("https://httpbin.org/get")
#data = response.json()['form']
#print(response.content()['form'])
#print(response.content)

#print(response.json()['current_user_url'])
print(response.status_code)
print(response.text)
print(response.json()['origin'])
#print(response.json())
#print(response.json()['origin'])
