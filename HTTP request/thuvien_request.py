import requests

url = "https://www.example.com/api/get_data"
headers =""
response = requests.get(url=url,headers=headers)

#print(response.json())
#chưa bt trường hợp trả về in hết
status= response.json
#data = response.json()
print(status)




