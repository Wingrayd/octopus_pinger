import socket
import json
import threading

def server_start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 30000))
    server_socket.listen(40)
    print("Сервер запущен и ожидает подключений...")
    client_connect(server_socket)

def client_connect(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Клиент подключился: {client_address}") 
        thread = threading.Thread(target=monitoring, args=(client_socket, server_socket, client_address))
        thread.start()

def monitoring(client_socket, server_socket, client_address):
    addrs = ['192.168.1.169', '192.168.1.170', '192.168.1.171']
    json_addrs = json.dumps(addrs)
    client_socket.send(json_addrs.encode())
    while True:
        data = client_socket.recv(1024)
        print(data.decode())
        if not data:
            print(f"Клиент отключился: {client_address}")
            break

server_start()
