'''
    TODO:
    - Design UI
    - Login, signup for client
''' 
import socket
from client_utils import *

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

    print("[CLIENT SIDE]")
    client.connect((cfg['HOST'], cfg['SERVER_PORT']))
    print('Client address:', client.getsockname())
    print('='*40)
    welcome_msg = client.recv(1024).decode(cfg['FORMAT'])
    answer_response(client, cfg['FORMAT'])
    print(welcome_msg)

    msg = None
    while msg != "close":
        request = client.recv(1024).decode(cfg['FORMAT'])
        print(request)
        msg = input("input: ")
        if msg == "phone_book_data":
            data = ask_phone_book_data(client)
            print(data)
        if msg == "close":
            client.sendall("close".encode(cfg['FORMAT']))

    client.close()