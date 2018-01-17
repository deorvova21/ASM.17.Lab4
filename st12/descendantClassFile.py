from  .myClassFile import myClass
import urllib.request as rq

class descendantClass(myClass):

    def __init__(self,q,givenName,givenParam,givenAdditionalAttribute,givenSecondAdditionalAttribute):
        self.name = givenName
        self.param = givenParam
        self.additionalAttribute=givenAdditionalAttribute
        self.secondAdditionalAttribute=givenSecondAdditionalAttribute

    def addInBase(self, myNymber):
        print("Отправляем потомка")
        rq.urlopen("http://localhost:81/cgi-bin/lab3.py?name='{0}'&param='{1}'&additionalAttribute={2}&secondAdditionalAttribute={3}&secondAction=addDescendantClass&action=addDescendantClass&student={4}".format(self.name, self.param,self.additionalAttribute,self.secondAdditionalAttribute, myNymber))

