import socket 

HOST = "localhost" 
PORT = 1234

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as f :
    f.connect((HOST,PORT))
    f.sendall(b"Hello,World!")
    data = f.recv(1024)

print("Yanıt",repr(data))
