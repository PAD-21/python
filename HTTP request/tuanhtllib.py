import httplib2

#url của trang web cần phải gửi yêu cầu tới
url = "https://actvn.edu.vn/"

# tạo đối tượng httplib2 http
http = httplib2.Http()

# gửi yêu cầu get đến url
response , content = http.request(url,"GET")

#in trạng thái của yêu cầu và nội dung của trang web
print(response.status)
print(content)
