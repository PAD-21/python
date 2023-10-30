import requests

response = requests.post("https://httpbin.org/post",data={"name":"thai","age":20})

#response = requests.post("https://httpbin.org/post",json={"name":"thai","age":20})

print(response.status_code)
print(response.text)
#print(response.json())
print(response.json()['json'])
