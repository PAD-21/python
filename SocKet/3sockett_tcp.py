import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((SERVER_IP,SERVER_PORT))
server.listen()

print("[*] Server listening on %s:%d" % (SERVER_IP,SERVER_PORT))
#print("server: ",SERVER_IP,SERVER_PORT)

client , addr = server.accept()
#print("client add",addr)
#print("client:",client.getsockname())

#message = client.recv(1024).decode(FORMAT)
client.send("I am the server accepting connections...".encode(FORMAT))
print("[*] Accepted connection from: %s:%d" %(addr[0],addr[1]))
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Received request : %s from  client %s" %(request, client_socket.getpeername()))
    client_socket.send("ACK".encode(FORMAT))
    while True:
        handle_client(client)
    
#client.sendall(message.encode(FORMAT))
#print("message: ",message)
input()