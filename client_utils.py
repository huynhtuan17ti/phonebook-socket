from utils import read_config, recieve_file, answer_response, receive_dict
from read import cfg

def receive_user_interface(connection):
    user_data = receive_dict(connection, cfg['FORMAT'])
    recieve_file(connection, 'client_data', cfg['FORMAT'], cfg['BUFFER_SIZE'])
    return user_data

def ask_phone_book_data(connection):
    connection.sendall("all_data".encode(cfg['FORMAT']))
    recv = connection.recv(1024).decode(cfg['FORMAT'])
    data_length = int(recv)
    answer_response(connection, cfg['FORMAT'])
    phone_book_data = []
    for _ in range(data_length):
        user_data = receive_user_interface(connection)
        phone_book_data.append(user_data)
    return phone_book_data