import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 65432))    

def listen():
    try:
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024)
        a = input('Enter the data to be sent to the client:')
        conn.sendall(a.encode())
        print(data.decode())
    except ex:
        print(ex)
        

while True:
    listen()