import socket
from utils import read_config, read_json, send_dict

cfg = read_config('config.yaml')
phone_book_data = read_json('data/phonebook.json')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

s.bind((cfg['HOST'], cfg['SERVER_PORT']))
s.listen()

print("[SEVER SIDE]")
print("Server:", cfg['HOST'], cfg['SERVER_PORT'])
print("Waiting for Client")

connection, addr = s.accept()

print("client address:", addr, "connected")
print("Connection:", connection.getsockname())


msg = None
while msg != "close":
    msg = connection.recv(1024).decode(cfg['FORMAT'])
    print("Client", addr, "sent:", msg)
    if msg == "get_data":
        send_dict(connection, phone_book_data, cfg['FORMAT'])