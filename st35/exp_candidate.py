import urllib.request as kod
from .candidate import Candidate

class Exp_Candidate(Candidate):

    def __init__(self):
        super().__init__()
        self.experience = ""
        self.last_job = ""

    def send(self, id):
        s = "&action=1&type=3&id=" + id + "&add=2&first_name=" + kod.quote(self.first_name) + "&last_name=" + kod.quote(
            self.last_name) + "&gender=" + kod.quote(self.gender)+ "&age=" + kod.quote(self.age) + "&mail=" + kod.quote(self.mail)  + "&experience=" + kod.quote(self.experience)  + "&last_job=" + kod.quote(self.last_job)
        return s
