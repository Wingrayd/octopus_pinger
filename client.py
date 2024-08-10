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
        json_addrs = client_socket.recv(1024)
        addrs = json.loads(json_addrs.decode())
        while True:
            pinging(addrs, client_socket)
    
def pinging(addrs, client_socket):
    for addr in addrs:
        result = ping(addr, count=1, timeout=1)
        if not result.success():
            result = ping(addr, count=3 , interval=0.5, timeout=2)
            if not result.success():
                data = bytes(f'{addr} is down', 'utf-8')
                try:
                    client_socket.send(data)
                except (socket.error) as e:
                    print(e)
                    server_connect()
        else :
            print(addr,' ok')

server_connect()