import re, urllib


class Sender:
    def __init__(self, url, student_number):
        self.url = url
        self.student_number = student_number

    def __find_student_id(self):
        data = urllib.request.urlopen(self.url)
        student_menu = str(data.read())
        id = re.search(r'student=(\d+)\">\[' + str(self.student_number) + '\]', student_menu).group(1)
        return id

    def send_container(self, container):
        id = self.__find_student_id()
        for card in container:
            card_parameters = card.get_parameters()
            full_url = self.url + f'?student={id}&card_id=-1&action=save_personal_card&'
            request = full_url + urllib.parse.urlencode(card_parameters)
            urllib.request.urlopen(request)
        print('Sent!')

