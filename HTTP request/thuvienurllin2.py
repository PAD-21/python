import httplib2
# gán url của trang web cần gửi vào biến url
url = "https://www.facebook.com/"

# tạo đối tượng Http từ thu viện httplib2 
http = httplib2.Http()

# gửi yêu cầu get đến url
response, content = http.request(url)

#in ra trạng thái của yêu cầu và nội dung của trang wed
print(response.status)
# print(content)