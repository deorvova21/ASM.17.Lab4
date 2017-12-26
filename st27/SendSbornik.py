import urllib


class SendSbornik:
    def __init__(self, url, common_params):
        self.url = url
        self.common_params = common_params

    def send(self, library):
        for sbornik in library:
            sbornik_info = sbornik.get_info()
            self.request(sbornik_info)
            print(str(sbornik) + ' отправлен!')
        print('Отправка всех Сборников закончена!')

    def request(self, sbornik_info):
        request = self.url + '?' + urllib.parse.urlencode(self.common_params) + \
                  '&' + urllib.parse.urlencode(sbornik_info)
        urllib.request.urlopen(request)
