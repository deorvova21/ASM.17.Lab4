from urllib.request import urlopen
import re


class Finder:
    def __init__(self, url):
        self.__url = url

    def find_student_num(self, student_id):
        response = urlopen(self.__url)
        content = str(response.read())
        student_num = re.search(r'student=(\d+)\">\[' + str(student_id) + '\]', content).group(1)
        return student_num
