class Person:
    def __init__(self, id: str, name: str, phone: str, gender: str, 
                        thumnail: str, image: str):
        self.id = id
        self.name = name
        self.phone = phone
        assert gender in ['Male', 'Female']
        self.gender = gender
        self.thumnail = thumnail
        self.image = image

    def to_dict(self):
        dt = {}
        dt['name'] = self.name
        dt['phone'] = self.phone
        dt['gender'] = self.gender
        dt['thumnail'] = self.thumnail
        dt['image'] = self.image
        return dt

    def get_id(self):
        return self.id