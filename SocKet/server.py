import socket

Host= "127.0.0.1" #loopback tro ve cai may cua minh
SERVER_PORT = 65432 # mở tren port
FORMAT = "utf8"

#đợi client kết nối vô
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #giao thuc tcp

s.bind((Host,SERVER_PORT)) #lang nghe den dia chi ip va cong
s.listen()

print("SERVER SIDE")
print("server:",Host,SERVER_PORT)
print("waiting for client")

#trao đổi thông tin trên đường truyền

conn, addr = s.accept()

print("client address:",addr)
print("conn:",conn.getsockname())


username = conn.recv(1024).decode(FORMAT)
conn.sendall(username.encode(FORMAT))

psw = conn.recv(1024).decode(FORMAT)

print("username:",username)
print("password:",psw)

input()

"""Dòngđầu tiên khai báo thư viện socket để sử dụng.
Biến Host và SERVER_PORT khai báo địa chỉ IP và cổng của máy chủ.
Biến FORMAT sử dụng để định dạng chuỗi thông điệp gửi đi và nhận về.
Hàm socket.socket() được sử dụng để tạo một socket với giao thức TCP (socket.AF_INET, socket.SOCK_STREAM) và lưu vào biến s.
Hàm bind() được sử dụng để liên kết địa chỉ IP và cổng của máy chủ với socket.
Hàm listen() được gọi để cho phép máy chủ lắng nghe các yêu cầu kết nối đến từ phía client.
Hàm accept() sẽ chờ đợi một kết nối từ client, sau đó trả về một đối tượng connection (conn) và địa chỉ của client (addr). Hàm này sẽ đơi đến khi có một kết nối mới được thực hiện đến socket của máy chủ.
Hàm recv() sử dụng để nhận thông điệp từ client với kích thước tối đa là 1024 bytes. Sau đó, thông điệp này sẽ được giải mã và gán vào biến username.
Hàm sendall() được sử dụng để gửi lại thông điệp cho client với định dạng chuỗi.
Tiếp theo, máy chủ tiếp tục nhận thông điệp từ client về mật khẩu của tài khoản.
Cuối cùng, hàm input() được sử dụng để giữ kết nối mở sau khi hoàn thành việc trao đổi thông tin giữa server và client.
"""