from .Native import Native


class Foreign(Native):
    def __init__(self, id, name, album_name, year, country):
        super().__init__(id, name, album_name, year)
        self.type = 'foreign'
        self.country = country
        
    def get_action():
        return 'insert_foreign'

    def get_data(self):
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'album_name': self.album_name,
            'year': self.year,
            'country': self.country
        }
