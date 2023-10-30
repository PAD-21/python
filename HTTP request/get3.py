import requests
# gửi yêu cầu đến trang chủ và lấy dữ liệu về
#đường dẫn xem địa chỉ ip của máy 
url = "https://httpbin.org/post"
headers=""
r=requests.post(url=url , headers=headers ,data={"name":"Duy","age":20})
#in trạng thái cập json kiêu dữ liệu của java scrip
print(r.status_code) #200 truy cập thành công , 400 k thể truy cập

#lấy dữ liệu 
data = r.text
print(data)