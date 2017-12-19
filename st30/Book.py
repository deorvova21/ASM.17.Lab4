class Book:
        title = ''
        cost = ''
        publishing_house = ''
        author = ''
        id_book = 0

        def generate_field(self):
                fields = {'title': self.title,'cost': self.cost,'publishing_house': self.publishing_house,'author': self.author}
                return fields

        def get_fields(self):
                fields = self.generate_field()
                fields['type'] = 'save_book'
                return fields

                
