'''
    TODO:
    - Design UI
    - Login, signup for client
''' 
import socket
from client_utils import *            
        
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

    print(cfg)

    print("[CLIENT SIDE]")
    
    while True:
        ip_addr = input('ip address: ')
        port_num = int(input('port number: '))
        try:
            client.connect((ip_addr, port_num))
            break
        except:
            print('Connection failed, please try again')
    
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