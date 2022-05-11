import socket
import json
from utils import read_config, recieve_file

cfg = read_config('config.yaml')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

print("[CLIENT SIDE]")
client.connect((cfg['HOST'], cfg['SERVER_PORT']))
print('Client address:', client.getsockname())

msg = None
while msg != "close":
    msg = input("input: ")
    client.sendall(msg.encode(cfg['FORMAT']))
    if msg in ['get_data', 'close']:
        data = client.recv(1024).decode(cfg['FORMAT'])
    if msg == 'get_file':
        recieve_file(client, 'client_data', cfg['FORMAT'], BUFFER_SIZE=cfg['BUFFER_SIZE'])


client.close()