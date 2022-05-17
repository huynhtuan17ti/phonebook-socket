'''
    TODO:
    - Design UI
    - Login, signup for client
''' 
import socket
from client_utils import *

def display_all(connection):
    data = ask_phone_book_data(connection)
    for item in data:
        print(item)
    
    print('='*40)
    while True:
        user_input = input('>> ')
        if user_input == 'back':
            break        
        
        if user_input == 'download thumbnails':
            receive_thumbnails(connection)
            continue
        
        token = user_input.split()
        
        if token[0] == 'query':
            ask_person_data(connection, token[1])
            
        
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

    print(cfg)

    print("[CLIENT SIDE]")
    client.connect((cfg['HOST'], cfg['SERVER_PORT']))
    print('Client address:', client.getsockname())
    print('='*40)
    welcome_msg = client.recv(1024).decode(cfg['FORMAT'])
    answer_response(client, cfg['FORMAT'])
    print(welcome_msg)

    while True:        
        user_input = input('> ')
        
        if user_input == 'login':
            display_all(client)
            
        if user_input == 'exit':
            client.recv(1024).decode(cfg['FORMAT'])
            client.sendall('close'.encode(cfg['FORMAT']))
            break
        

    client.close()