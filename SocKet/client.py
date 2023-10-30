import socket

Host = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("CLIENT SIDE")
client.connect((Host,SERVER_PORT))
print("client address:",client.getsockname())

username = input("username:")

psw = input("password:")


#gui la encode
client.sendall(username.encode(FORMAT))
client.recv(1024)

client.sendall(psw.encode(FORMAT))
input()

"""
import socket: Nhập thư viện socket để có thể sử dụng các hàm của socket trong Python.

Host = "127.0.0.1": Địa chỉ IP của máy chủ (localhost).

SERVER_PORT = 65432: Port mà máy chủ đang lắng nghe để kết nối.

FORMAT = "utf8": Định dạng được sử dụng để mã hóa và giải mã dữ liệu truyền qua đường truyền.

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM): Tạo một đối tượng socket mới để kết nối đến server, với giao thức TCP/IP (SOCK_STREAM).

client.connect((Host,SERVER_PORT)): Kết nối đến server với địa chỉ IP và port cụ thể.

print("client address:",client.getsockname()): In địa chỉ IP và port của client.

username = input("username:"): Nhập tên người dùng từ bàn phím.

psw = input("password:"): Nhập mật khẩu từ bàn phím.

client.sendall(username.encode(FORMAT)): Gửi tên người dùng đến server, được mã hóa theo định dạng đã chỉ định.

client.recv(1024): Chờ server gửi lại tên người dùng đã được xác thực.

client.sendall(psw.encode(FORMAT)): Gửi mật khẩu đến server, được mã hóa theo định dạng đã chỉ định.

input(): Chờ nhập bất cứ phím nào để kết thúc chương trình.
"""