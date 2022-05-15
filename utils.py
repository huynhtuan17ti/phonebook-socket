from tqdm import tqdm
import os
import yaml
import json
from typing import Dict

def read_config(config_file: str):
    with open(config_file) as f:
        return yaml.safe_load(f)

def read_json(json_file: str):
    with open(json_file) as f:
        return json.load(f)

def wait_response(connection, decode_format):
    if not connection.recv(1024).decode(decode_format) == 'received':
        print('[ERROR] Client not repsonding!')

def answer_response(connection, encode_format):
    connection.send("received".encode(encode_format))

def send_dict(connection, data_dict: Dict, encode_format: str):
    '''
        Send a dictionary object via connection
        ----------
        Parameters
        ----------
            - connection: connection is used to send
            - data_dict: dictionary object
            - encode_format: used in encoding
    '''
    data_string = json.dumps(data_dict)
    connection.sendall(data_string.encode(encode_format))
    wait_response(connection, encode_format)

def receive_dict(connection, decode_format: str):
    '''
        Receive a dictionary object via connection
        ----------
        Parameters
        ----------
            - connection: connection is used to send
            - decode_format: used in decoding
    '''
    data = connection.recv(1024).decode(decode_format)
    answer_response(connection, decode_format)
    return json.loads(data)

def send_file(connection, file_path: str, encode_format: str, BUFFER_SIZE: int = 1024):
    '''
        Send a file via connection
        ----------
        Parameters
        ----------
            - connection: connection is used to send
            - file_path: relative/absolute path of file
            - encode_format: used in encoding
            - BUFFER_SIZE: maximum capacity sent of a single iteration
    '''
    print(f'[-] Sending {file_path} ...', end=' ')
    file_size = os.path.getsize(file_path)
    # send file name and file size
    connection.send(f"{file_path.split('/')[-1]} {file_size}".encode(encode_format))
    wait_response(connection, encode_format)
    with open(file_path, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            connection.sendall(bytes_read)
    wait_response(connection, encode_format)
    print('Successfully!')

def recieve_file(connection, file_dir: str, decode_format: str, BUFFER_SIZE: int = 1024):
    '''
        Receive a file via connection
        ----------
        Parameters
        ----------
            - connection: connection is used to send
            - file_dir: directory to save the file
            - decode_format: used in decoding
            - BUFFER_SIZE: maximum capacity sent of a single iteration
    '''
    received = connection.recv(BUFFER_SIZE).decode(decode_format)
    answer_response(connection, decode_format)
    print(f'[+] Receiving', end=' ')
    file_path, file_size = received.split()
    print(f'{file_path} from server ...', end=' ')
    file_size = int(file_size)
    total_size = 0
    with open(os.path.join(file_dir, file_path), "wb") as f:
        while True:
            if total_size >= file_size:
                break
            # read BUFFER_SIZE bytes from the socket (receive)
            bytes_read = connection.recv(BUFFER_SIZE)
            total_size += len(bytes_read)
            f.write(bytes_read)
    answer_response(connection, decode_format)
    print(f'Successfully!')