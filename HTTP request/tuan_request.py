import requests
# gửi yêu cầu đến trang chủ và lấy dữ liệu về
#đường dẫn xem user vừa dk nik tren github
url = "https://api.github.com/events"

r=requests.get(url=url )
#in trạng thái cập json kiêu dữ liệu của java scrip
status=r.json  #200 truy cập thành công , 400 k thể truy cập
#lấy dữ liệu , lấy ra sự kiện mới nhất
data = r.json()[0]["actor"]
print(status)
print(data)


# print(r.status_code)   # in ra  mã trạng thái
# print(r.encoding)      # in ra mã hóa hóa của trang web
# print(r.elapsed)       # in ra thời gian giữa gửi yêu cầu và nhận phản hồi
# print(r.url)           # in ra đường dẫn sau cùng 
