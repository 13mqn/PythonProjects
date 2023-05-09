import socket

HOST = "localhost" 
PORT = 1234


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print (f"Dinleme başlatıldı ! {HOST},{PORT}")

    while True:
        conn , addr = s.accept()
        print(f"Bağlantı kabul edildi! ({addr[0]}:{addr[1]})") 
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print (f"gelen veri : {data.decode()}")

