class Department():
    def __init__(self, id='', nickname='', owner_name='', product_type='', address=''):
        self.id = id
        self.type = 'department'
        self.nickname = nickname
        self.owner_name = owner_name
        self.product_type = product_type
        self.address = address

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
        print('<input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')

    def read(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.nickname = self.q['nickname'].value
        self.owner_name = self.q['owner_name'].value
        self.product_type = self.q['product_type'].value
        self.address = self.q['address'].value
        
    def show(self):
        print("<br>Название отдела: {0} | ФИО владельца отдела: {1} | Виды продаваемых продуктов: {2} | Адрес магазина: {3}".format(self.nickname,self.owner_name,self.product_type,self.address))
