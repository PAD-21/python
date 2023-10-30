import requests
import os
import shodan

#SHODAN_API_KEY =  
print(os.environ['SHODAN_API_KEY'])

ip = "1.1.1.1"

def ShodanInfo(ip):
    try:
        result = requests.get("https:api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minify=True").json()
    except Exception as exception:
        reuslt = {"error":"Information not available"}
    return result
print(ShodanInfo(ip))

"""
Đăng nhập vào tài khoản Shodan và truy cập trang User Settings.

Tìm đến phần API Key và nhấn Generate API Key để tạo ra một khóa API.

Sao chép khóa API và dán vào một tệp tin văn bản tạm thời.

Mở terminal hoặc command prompt trên hệ thống của bạn.

Thiết lập biến môi trường SHODAN_API_KEY bằng cách chạy lệnh export SHODAN_API_KEY=<khóa API của bạn> 
trên Linux hoặc MacOS, hoặc lệnh set SHODAN_API_KEY=<khóa API của bạn> trên Windows. 
Chú ý rằng, các lệnh này sẽ khởi tạo biến môi trường SHODAN_API_KEY với giá trị là khóa API của bạn.

Kiểm tra xem biến môi trường SHODAN_API_KEY đã được thiết lập đúng bằng cách chạy lệnh echo $SHODAN_API_KEY trên Linux hoặc MacOS, hoặc lệnh echo %SHODAN_API_KEY% trên Windows. Nếu giá trị được hiển thị là khóa API của bạn, thì biến môi trường đã được thiết lập đúng.
"""
