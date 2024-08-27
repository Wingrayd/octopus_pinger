import socket
import json
import threading
import multiprocessing
from multiprocessing import Queue
import mysql.connector
import time

def server_start(queue):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 30000))
    server_socket.listen(40)
    print("Сервер запущен и ожидает подключений...")
    client_connect(server_socket, queue)

def client_connect(server_socket, queue):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Клиент подключился: {client_address}") 
        database = mysql.connector.connect(user='root', password='7702', host='localhost', port='3306', database='pinger')
        cursor = database.cursor()
        query = (f"SELECT DISTINCT t.IP FROM DCTargets t INNER JOIN DCServers s ON t.id = s.id WHERE s.IP = '{client_address[0]}';")
        cursor.execute(query)
        addrs = cursor.fetchall()
        cursor.close()
        database.close()
        thread = threading.Thread(target=monitoring, args=(client_socket, client_address, queue, addrs))
        thread.start()

def monitoring(client_socket, client_address, queue, addrs):
    print(addrs)
    json_addrs = json.dumps(addrs)
    client_socket.send(json_addrs.encode())
    host = client_address[0]
    while True:
        global problems
        if host not in problems:
            problems[host] = []
            queue.put(problems)
        else:
            data = client_socket.recv(1024)
            if not data:
                print(f"Клиент отключился: {client_address}")
                problems.pop(host)
                queue.put(problems)
                break
            silent = json.loads(data.decode())
            if silent != True:
                problems[host] = (silent)
                queue.put(problems)
            

################################################################################


def test(queue):
    while True:
        problems = queue.get()
        print(problems)


problems = {}
queue = Queue()
server_play = multiprocessing.Process(target=server_start, args=(queue,))
interface = multiprocessing.Process(target=test, args=(queue,))
server_play.start()
interface.start()
server_play.join()
interface.join()
