from .MobilePhone import MobilePhone


class SmartPhone(MobilePhone):
    def __init__(self, id, brand, screen_size, housing_type, os, ram):
        super().__init__(id, brand, screen_size, housing_type)
        self.type = 'smart_phone'
        self.os = os
        self.ram = ram

    def get_data(self):
        return {
            'id': self.id,
            'type': self.type,
            'brand': self.brand,
            'screen_size': self.screen_size,
            'housing_type': self.housing_type,
            'os': self.os,
            'ram': self.ram
        }
