from .department import Department


class Seller(Department):
     
    def __init__(self, id='', nickname='', owner_name='', product_type='', address='', name_seller='', tel=''):
        super().__init__(id,nickname, owner_name, product_type , address)
        self.type = 'seller'
        self.name_seller = name_seller
        self.tel = tel 

    def form(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table cellpadding="7" border="1"><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "id" value = "{0}" >'.format(self.q.getvalue('id')))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Название отдела: ')
        print('<input type = "text" name = "nickname" value="{0}">'.format(self.nickname))
        print('ФИО владельца отдела:')
        print('<input type = "text" name = "owner_name" value="{0}">'.format(self.owner_name))
        print('Виды продаваемых продуктов: ')
        print('<input type = "text" name = "product_type" value="{0}">'.format(self.product_type))
        print('Адрес магазина: ')
        print('<input type = "text" name = "address" value="{0}">'.format(self.address))
        print('ФИО продавца: ')
        print('<input type = "text" name = "name_seller" value="{0}">'.format(self.name_seller))
        print('Номер телефона продавца: ')
        print('<input type = "text" name = "tel" value="{0}">'.format(self.tel))
        print('<input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')

    def read(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.nickname=self.q['nickname'].value
        self.owner_name = self.q['owner_name'].value
        self.product_type = self.q['product_type'].value
        self.address = self.q['address''].value
        self.name_seller = self.q['name_seller'].value
        self.tel = self.q['tel'].value

    def show(self):
        print("<br>Название отдела: {0} | ФИО владельцп отдела: {1} | Виды продаваемых продуктов: {2} | Адрес магазина: {3} | ФИО продавца: {4} | Номер телефона продавца: {5}".format(self.nickname,self.owner_name,self.product_type,self.address,self.name_seller,self.tel))
