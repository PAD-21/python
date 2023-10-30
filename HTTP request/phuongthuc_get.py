import requests
# gửi yêu cầu đến trang chủ và lấy dữ liệu về
#đường dẫn xem địa chỉ ip của máy 
url = "https://api.ipify.org/"
headers=""
r=requests.get(url=url , headers=headers)
#in trạng thái cập json kiêu dữ liệu của java scrip
status=r.json  #200 truy cập thành công , 400 k thể truy cập

#lấy dữ liệu 
data = r.text
print(status)
print(data)

