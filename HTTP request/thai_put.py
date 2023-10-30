import requests

response = requests.put("https://httpbin.org/put",data={"name":"thai","age":20,"pwd":123})

print(response.status_code)

print(response.text)
