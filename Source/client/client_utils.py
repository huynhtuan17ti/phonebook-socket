from utils import receive_file, answer_response, receive_dict
from read import cfg

def receive_user_interface(connection):
    user_data = receive_dict(connection, cfg['FORMAT'])
    return user_data

def ask_phone_book_data(connection):
    msg = connection.recv(1024).decode(cfg['FORMAT'])
    print(msg)
    
    connection.sendall("all data".encode(cfg['FORMAT']))
    recv = connection.recv(1024).decode(cfg['FORMAT'])
    data_length = int(recv)
    answer_response(connection, cfg['FORMAT'])
    phone_book_data = []
    for _ in range(data_length):
        user_data = receive_user_interface(connection)
        phone_book_data.append(user_data)
    return phone_book_data

def receive_user_image(connection, person_id):
    greet_msg = connection.recv(1024).decode(cfg['FORMAT'])
    print(greet_msg)
    
    connection.sendall(f'image {person_id}'.encode(cfg['FORMAT']))
    
    exist = connection.recv(1024).decode(cfg['FORMAT'])
    
    if exist == 'false':
        return
    
    receive_file(connection, 'client_data/images', cfg['FORMAT'], cfg['BUFFER_SIZE'])
    

def ask_person_data(connection, person_id):
    greet_msg = connection.recv(1024).decode(cfg['FORMAT'])
    print(greet_msg)
    
    connection.sendall(f'detail {person_id}'.encode(cfg['FORMAT']))
    data = receive_user_interface(connection)
    
    print(data)
    
    if not data:
        return
    
    while True:
        user_input = input('>>> ')
        
        if user_input == 'download image':
            receive_user_image(connection, person_id)
        
        if user_input == 'back':
            break
        
    return data

def receive_thumbnails(connection):
    greet_msg = connection.recv(1024).decode(cfg['FORMAT'])
    print(greet_msg)
    
    connection.sendall('all thumbnails'.encode(cfg['FORMAT']))
    
    data_length = int(connection.recv(1024).decode(cfg['FORMAT']))
    answer_response(connection, cfg['FORMAT'])

    cnt = 0
    for _ in range(data_length):
        receive_file(connection, 'client_data/thumbnails', cfg['FORMAT'], cfg['BUFFER_SIZE'])
        
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
