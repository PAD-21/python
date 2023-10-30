import requests
from requests.auth import HTTPDigestAuth #một phương pháp xác thực trong giao thức HTTP để bảo mật 
                                        #các truy cập vào tài nguyên web.
from getpass import getpass
user = input("Nhập user:")
pwd = getpass()
url = "http://httpbin.org/digest-auth/auth/user/pass"
response = requests.get(url, auth = HTTPDigestAuth(user,pwd))

print("Headers request: ")
for header, value in response.request.headers.items():
    print(header, "-->" , value)
print("Response.status_code: "+str(response.status_code))

if response.status_code ==200:
    print("Login sucessful : "+str(response.json()))

print("Headers response: ")
for header , value in response.headers.items():
    print(header, "-->" , value)

"""

Import thư viện requests và HTTPDigestAuth từ requests.auth.
Import getpass để yêu cầu người dùng nhập mật khẩu một cách bảo mật và lưu trữ nó trong biến pwd.
Yêu cầu người dùng nhập tên đăng nhập (user) và lưu trữ nó trong biến user.
Xác định URL của tài nguyên web được bảo mật.
Sử dụng phương thức get của requests với đối số auth là một đối tượng HTTPDigestAuth được tạo với tên đăng nhập và 
mật khẩu của người dùng. Kết quả trả về được lưu trữ trong biến response.
In ra các header của yêu cầu (request) bằng cách lặp qua các mục của response.request.headers.
In ra mã trạng thái HTTP của response.
Nếu mã trạng thái là 200 (nghĩa là thành công), in ra dữ liệu trả về của yêu cầu bằng cách gọi phương thức json() 
của response.
In ra các header của phản hồi (response) bằng cách lặp qua các mục của response.headers.


khi một client yêu cầu truy cập một tài nguyên được bảo vệ, 
server sẽ gửi lại cho client một phản hồi yêu cầu xác thực. 
Phản hồi này bao gồm một thách thức (challenge) chứa các thông tin như tên người dùng, 
một mảng các giá trị băm (hash) và một khóa (nonce) ngẫu nhiên. 
Client sẽ sử dụng thông tin này để tạo ra một thông điệp xác thực (authentication message) 
bao gồm tên người dùng, mật khẩu và một số thông tin bổ sung, sau đó gửi lại cho server. 
Server sẽ kiểm tra thông điệp xác thực này và trả về trạng thái thành công hoặc thất bại cho client.
"""