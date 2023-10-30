import socket
SERVER_IP= "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((SERVER_IP,SERVER_PORT))
#print("client add",mysocket.getsockname())
print("Connected to host "+str(SERVER_IP)+" in port:"+str(SERVER_PORT))
message = mysocket.recv(1024)
print("Message recevid from the server",message)
while True:
    message = input("Enter your message > ")
    mysocket.send(bytes(message.encode(FORMAT)))
    #print("Message recevid from the server ", mysocket.recv(1024))
    if message=="quit":
        break
#mysocket.recv(1024)


input()