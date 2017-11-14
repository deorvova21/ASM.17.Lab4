import urllib.request

class Category:
    def __init__(self):
        self.tittle = ""

    def send(self):
        rec="tittle="+urllib.request.quote(self.tittle)
        return rec
