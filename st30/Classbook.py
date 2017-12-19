from .Book import Book


class Classbook(Book):
	subject = ''

	def get_fields(self):
                fields = self.generate_field()
                fields['subject'] = self.subject
                fields['type'] = 'save_book'
                return fields
