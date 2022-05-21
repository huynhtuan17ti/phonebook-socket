import json
from object import Person

phone_book_list = [
    Person('p01', 'Kkura', '0357933544', 'Male', '', ''),
    Person('p02', 'Kkura1', '0357933544', 'Male', '', ''),
    Person('p03', 'Kkura2', '0357933544', 'Male', '', ''),
    Person('p04', 'Kkura3', '0357933544', 'Female', '', ''),
]

phonebook_dict = {}
for person in phone_book_list:
    phonebook_dict[person.get_id()] = person.to_dict()

with open('data/phonebook.json', 'w') as f:
    json.dump(phonebook_dict, f)