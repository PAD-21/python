import socket
try:
    print("gethostname:",socket.gethostname)
    print("gethostbyname",socket.gethostbyname("www.actvn.edu.vn"))
    print("gethostbyname_ex",socket.gethostbyname_ex("www.actvn.edu.vn"))
    print("gethostaddr",socket.gethostbyaddr("103.21.148.154"))
    print("getfqdn",socket.getfqdn("www.actvn.edu.vn"))
    print("getaddrinfo",socket.getaddrinfo("www.actvn.edu.vn",None,0,socket.SOCK_STREAM))
except socket.error as error:
    print(str(error))
    print("Connection error")

"""
Đoạn mã Python này sử dụng module socket để thực hiện các tác vụ liên quan đến mạng.

Module socket cung cấp một giao diện cấp thấp cho việc giao tiếp mạng sử dụng giao thức TCP/IP.
Hàm gethostname() trả về tên máy chủ của hệ thống hiện tại.
Hàm gethostbyname() nhận đầu vào là tên máy chủ và trả về địa chỉ IP của máy chủ đó. Trong trường hợp này, tên máy chủ là "www.actvn.edu.vn".
Hàm gethostbyname_ex() thực hiện tương tự như gethostbyname(), nhưng trả về thông tin bổ sung dưới dạng tuple, bao gồm các tên định danh và địa chỉ IP.
Hàm gethostbyaddr() nhận đầu vào là địa chỉ IP và trả về tên máy chủ tương ứng với địa chỉ IP đó.
Hàm getfqdn() trả về tên miền đầy đủ (FQDN) của một máy chủ.
Hàm getaddrinfo() là một hàm nâng cao hơn, thực hiện tìm kiếm DNS và trả về danh sách các tuple chứa các thông tin khác nhau về địa chỉ, bao gồm địa chỉ IP và số cổng.
Nếu xảy ra bất kỳ lỗi nào trong quá trình thực thi mã, ngoại lệ socket.error sẽ được bắt và một thông báo lỗi sẽ được in ra.


"""
