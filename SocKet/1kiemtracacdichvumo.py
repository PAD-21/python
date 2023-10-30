import socket
ip = "42.113.206.26"
portlist = [21,22,23,80,443]
for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #tcp
    result = sock.connect_ex((ip,port))
    print(port,":",result)
    sock.close()
"""
    Đầu tiên, mã nhập thư viện socket.

Sau đó, nó thiết lập biến ip với địa chỉ IP mục tiêu.

Mã tạo một danh sách các cổng mục tiêu được gọi là portlist, mà nó sẽ lặp lại để thử kết nối.

Đối với mỗi cổng trong danh sách cổng, mã tạo một đối tượng socket bằng cách sử dụng socket.socket(), chỉ định họ địa chỉ là AF_INET và kiểu socket là SOCK_STREAM.

Tiếp theo, phương thức connect_ex() được gọi trên đối tượng socket, chuyển địa chỉ IP và cổng mục tiêu. 
Phương thức này cố gắng thiết lập kết nối với địa chỉ và cổng được chỉ định.

Phương thức connect_ex() trả về mã kết quả. Nếu kết nối thành công, kết quả sẽ là 0. Nếu kết nối thất bại, kết quả sẽ là mã lỗi.

Mã sau đó in ra số cổng và mã kết quả cho mỗi kết nối được thử bằng cách sử dụng print().

Cuối cùng, mã đóng socket bằng cách sử dụng sock.close() sau khi thử kết nối cho mỗi cổng trong danh sách portlist.

"""

