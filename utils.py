from http import client
from matplotlib.font_manager import json_dump
import yaml
import json
from typing import Dict

def read_config(config_file: str):
    with open(config_file) as f:
        return yaml.safe_load(f)

def read_json(json_file: str):
    with open(json_file) as f:
        return json.load(f)

def send_dict(connection, data_dict: Dict, encode_format: str, key: str = None):
    if key == None:
        data_string = json.dumps(data_dict)
    else:
        data_string = json_dump(data_dict[key])

    connection.sendall(data_string.encode(encode_format))
    # connection.send("end".encode(encode_format))