import urllib.request as kod

class Candidate:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.gender = ""
        self.age = ""
        self.mail = ""

    def send(self, id):
        s = "&action=1&type=3&id=" + id + "&add=1&first_name=" + kod.quote(self.first_name) + "&last_name=" + kod.quote(
            self.last_name) + "&gender=" + kod.quote(self.gender)+ "&age=" + kod.quote(self.age) + "&mail=" + kod.quote(self.mail)
        return s