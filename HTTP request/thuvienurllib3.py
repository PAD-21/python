import urllib.request  # cung cấp các hàm gửi tới url
import urllib.parse   # chứa các hàm để phần tích và chuyển đổi url

#url của trang web cần gửi yêu cầu tới
url = "https://actvn.edu.vn/"

#Dữ liệu cần gửi kèm theo yêu cầu
data = {"keyword": "example"}

# Mã hóa dữ liệu thành dạng url
data = urllib.parse.urlencode(data).encode("utf-8")

#tạo đối tượng request
request = urllib.request.Request(url,data)

# gửi yêu cầu post đến url
response = urllib.request.urlopen(request)

# đọc nội dung của trang web
content = response.read().decode("utf-8")

#in nội dung
print(response.getcode())
print(content)