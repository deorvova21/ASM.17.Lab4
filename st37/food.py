import urllib

class food:

    def __init__(self):
        
        self.name = ""
        self.quantity = ""
        self.calories = ""


    def peredacha(self):
        inform = "&name="+urllib.quote(self.name)+"&quantity="+urllib.quote(self.quantity)+"&calories="+urllib.quote(self.calories)
        return inform
    
