class Sbornik:
    name = 'None'
    developer = 'None'
    date = 'None'

    def get_info(self):
        return {'name': self.name, 'developer': self.developer, 'date': self.date, 'sb_fl': 0}

    def __str__(self):
        return self.name
