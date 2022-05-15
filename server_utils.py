from utils import send_dict, send_file, wait_response
from read import *

# ---- SERVER UTILS ----
def send_phone_book_data(connection):
    connection.send(f"{len(phone_book_data)}".encode(cfg['FORMAT']))
    wait_response(connection, cfg['FORMAT'])
    for user_id in phone_book_data.keys():
        send_user_interface(connection, user_id)
        
def send_user_interface(connection, user_id: str):
    send_dict(connection, phone_book_data[user_id], cfg['FORMAT'])
    send_user_thumnail(connection, user_id)

def send_user_thumnail(connection, user_id: str):
    send_file(connection, phone_book_data[user_id]['thumnail'], cfg['FORMAT'], cfg['BUFFER_SIZE'])

def send_user_image(connection, user_id: str):
    send_file(connection, phone_book_data[user_id]['image'], cfg['FORMAT'], cfg['BUFFER_SIZE'])