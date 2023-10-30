#Lập trinh đa luồng - tạo nhiều client kết nối vô 1 server
import socket
import threading
HOST = "127.0.0.1"  # địa chỉ lookBack
SERVER_PORT  = 65432
FORMAT = "utf8"

def handleClient(con: socket, addr):
    print("con:" , con.getsockname())

    msg = None
    while(msg !="Exit"):
        msg = con.recv(1024).decode(FORMAT)
        print("say: " , msg)
    
    print("client " , addr , "finish")
    print(con.getsockname() , "closed")
    con.close() 

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #giao thức tcp

s.bind((HOST , SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:", HOST , SERVER_PORT)
print("waiting for client")

nclient = 0
while(nclient < 3):
    try:
        con , addr = s.accept()
        thr = threading.Thread(target=handleClient , args=(con,addr))
        thr.daemon = True
        thr.start()
        
    except:
        print("Errorr")
    
    nclient+=1

print("End")
input()
s.close()

"""
Đây là một ví dụ đơn giản về lập trình đa luồng trong Python sử dụng module socket và threading. Mục tiêu của chương trình là tạo ra một server đơn giản cho phép nhiều client kết nối đến và gửi tin nhắn.

Khởi tạo các biến và hằng số:
HOST: địa chỉ IP loopback (127.0.0.1) cho server.
SERVER_PORT: cổng mạng để lắng nghe kết nối từ các client.
FORMAT: định dạng chuỗi để mã hóa và giải mã các tin nhắn.
Định nghĩa hàm handleClient:
Hàm này được sử dụng để xử lý các tin nhắn từ client.
Tham số đầu vào của hàm là con (socket) và addr (địa chỉ IP của client).
Hàm này sẽ lặp lại việc nhận các tin nhắn từ client cho đến khi client gửi tin nhắn "Exit".
Sau đó, hàm này sẽ đóng kết nối và in ra thông báo về client đã kết thúc.
Tạo socket và lắng nghe các kết nối:
Đầu tiên, chương trình tạo một socket với giao thức TCP và bind nó vào địa chỉ và cổng được xác định ở trên.
Sau đó, chương trình sử dụng hàm listen để lắng nghe kết nối từ các client.
Xử lý các kết nối:
Vòng lặp while được sử dụng để lặp lại việc chấp nhận các kết nối từ client.
Khi có một kết nối mới, chương trình chấp nhận nó và tạo một luồng mới để xử lý các tin nhắn từ client.
Hàm threading.Thread được sử dụng để tạo một luồng mới, với hàm handleClient làm đối số.
Hàm setDaemon(True) được sử dụng để thiết lập luồng này là một luồng chủ động.
Sau khi tạo luồng mới, chương trình tăng giá trị biến nclient lên 1.
Đóng kết nối và kết thúc chương trình:
Khi số lượng client đã kết nối đủ, vòng lặp sẽ kết thúc và chương trình sẽ in ra thông báo "End".
Cuối cùng, chương trình sử dụng hàm input để giữ chương trình chạy cho đến khi người dùng nhấn Enter.
Cuối cùng, chương trình đóng kết nối với socket.
"""
