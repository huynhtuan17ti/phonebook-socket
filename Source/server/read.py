'''
    Read config and database
'''
from utils import read_config, read_json
cfg = read_config('config.yaml')
phone_book_data = read_json('server_data/phonebook.json')