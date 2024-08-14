import socket
import json
import threading
import multiprocessing
import time

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
        thread = threading.Thread(target=monitoring, args=(client_socket, client_address))
        thread.start()

def monitoring(client_socket, client_address):
    addrs = ['192.168.1.169', '192.168.1.170', '192.168.1.171']
    json_addrs = json.dumps(addrs)
    client_socket.send(json_addrs.encode())
    host = client_address[0]
    while True:
        global problems
        if host not in problems:
            problems[host] = []
            print(problems)
        else:
            data = client_socket.recv(1024)
            if not data:
                print(f"Клиент отключился: {client_address}")
                problems.pop(host)
                print(problems)
                break
            silent = json.loads(data.decode())
            if silent != 47:
                problems[host] = (silent)
                print(problems)
            

################################################################################


def test():
    while True:
        global problems
    #    print(problems)
        time.sleep(1)


problems = {}
server_play = multiprocessing.Process(target=server_start)
interface = multiprocessing.Process(target=test)
server_play.start()
interface.start()
server_play.join()
interface.join()
