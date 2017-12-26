from .Sbornik import *


class MestSbornik(Sbornik):
    organization = 'None'

    def get_params(self):
        return {'name': self.name, 'developer': self.developer, 'date': self.date, 'organization': self.organization, 'sb_fl': 1}
