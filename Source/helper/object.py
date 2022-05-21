class Person:
    def __init__(self, id: str, name: str, phone: str, gender: str, 
                        thumbnail: str, image: str):
        self.id = id
        self.name = name
        self.phone = phone
        assert gender in ['Male', 'Female']
        self.gender = gender
        self.thumbnail = thumbnail
        self.image = image

    def to_dict(self):
        dt = {}
        dt['name'] = self.name
        dt['phone'] = self.phone
        dt['gender'] = self.gender
        dt['thumbnail'] = self.thumbnail
        dt['image'] = self.image
        return dt

    def get_id(self):
        return self.id