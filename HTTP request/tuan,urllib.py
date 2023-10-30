import urllib.request
#  mở kết nối tới một URL bằng urllib
webUrl  = urllib.request.urlopen('https://actvn.edu.vn/')

#lấy mã kết quả và in nó
print ("result code: " + str(webUrl.getcode()))

# đọc dữ liệu từ URL và in nó
data = webUrl.read()

print (data)




