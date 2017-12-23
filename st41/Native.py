class Native:
    def __init__(self, id, name, album_name, year):
        self.id = id
        self.type = 'native'
        self.name = name
        self.album_name = album_name
        self.year = year

    def get_data(self):
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'album_name': self.album_name,
            'year': self.year
        }
