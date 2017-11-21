class MobilePhone:
    def __init__(self, id, brand, screen_size, housing_type):
        self.id = id
        self.type = 'mobile_phone'
        self.brand = brand
        self.screen_size = screen_size
        self.housing_type = housing_type

    def get_data(self):
        return {
            'id': self.id,
            'type': self.type,
            'brand': self.brand,
            'screen_size': self.screen_size,
            'housing_type': self.housing_type
        }
