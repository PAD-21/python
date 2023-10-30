#tạo một kênh chat giữa server và client
import socket

HOST = "127.0.0.1"  # địa chỉ lookBack
SERVER_PORT  = 65432
FORMAT = "utf8"

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #giao thức tcp

s.bind((HOST , SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:", HOST , SERVER_PORT)
print("waiting for client")

try:
    con , addr = s.accept()
    print("Client address:" , addr)
    print("con:" , con.getsockname())

    msg = None
    while(msg !="Exit"):
        msg = con.recv(1024).decode(FORMAT)
        print("say: " , msg)
        msg = input("server response: ")
        con.sendall(msg.encode(FORMAT))
except:
    print("Errorr")

print("End")
input()
con.close()


