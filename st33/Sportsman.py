class Sportsman:
    def __init__(self):
        self._full_name = None
        self._age = None
        self._rating = None

    def getFull_name(self):
        return self._full_name

    def getAge(self):
        return self._age

    def getRating(self):
        return self._rating

    def send():
        return "&full_name=" + urllib.parse.quote(str(e.getFull_name())) + "&age=" + urllib.parse.quote(str(e.getAge())) + "&rating=" + urllib.parse.quote(str(e.getRating()))
