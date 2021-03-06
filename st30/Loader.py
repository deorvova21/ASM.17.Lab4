import http.client
from st30.function import *
import pickle
import re
import urllib.request
import urllib.parse


class Loader():
	url = 'http://localhost:81/cgi-bin/lab3.py'
	__base = []

	def __init__(self):
		res = urllib.request.urlopen(self.url)
		lab3 = str(res.read())
		res.close()
		self.student_id = re.search(r'student=(\d+)\">\[30\]', lab3).group(1)

	def save(self):
		while (True):
			file_name = input('Enter file name\n')
			if (is_file(file_name)):
				with open(str(file_name) + '.dat', 'rb') as f:
					self.__base = pickle.load(f)
				break
			else:
				print('Error reading the file')
				answer = input('Want to repeat again?\nYes/No')
				if (str.lower(answer) != 'yes'):
					break
		try:
			for book in self.__base:
				fields = book.get_fields()
				fields['student'] = self.student_id
				fields['id_book'] = 0
				request_url = self.url + '?' + urllib.parse.urlencode(fields)
				urllib.request.urlopen(request_url)
		except Exception as e:
			print(e)
