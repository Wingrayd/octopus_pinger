import socket
from pythonping import ping
import json
import time

def server_connect():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.1.113', 30000))
    except (socket.error, ConnectionRefusedError) as e:  
        print(e)
        time.sleep(10)
        server_connect()
    else: 
        data = client_socket.recv(1024)
        addrs = json.loads(data.decode())
        silent = []
        while True:
            pinging(addrs, client_socket, silent)

def pinging(addrs, client_socket, silent):
    for addr in addrs:
        result = ping(addr[0], count=1, timeout=1)
        
        if not result.success():
            if addr not in silent:
                silent.append(addr)
                sending(client_socket, silent) 
            #print(addr,' down')
        else :
            if addr in silent:
                silent.remove(addr)
                sending(client_socket, silent)
            #print(addr,' ok')
    check = json.dumps(True)
    try:
        client_socket.send(check.encode())
    except (socket.error) as err:
            print(err)
            server_connect()

def sending(client_socket, silent):
    json_silent = json.dumps(silent)
    try:
        client_socket.send(json_silent.encode())
    except (socket.error) as err:
            print(err)
            server_connect()

server_connect()
