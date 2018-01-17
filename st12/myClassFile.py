import urllib.request as rq

class myClass:

    def __init__(self,q,givenName,givenParam):
         self.name =givenName
         self.param =givenParam

    def addInBase(self,myNymber):
        print("Отправляем предка:{0},{1}".format(self.name,self.param))
        requesturl="http://localhost:81/cgi-bin/lab3.py?name={0}&param={1}&secondAction=addClass&action=addClass&student={2}".format(self.name,self.param,myNymber)
        print(requesturl)
        rq.urlopen(requesturl)


