from urllib.request import urlopen
from urllib.parse import urlencode


class HttpCarImporter:
    def __init__(self, url):
        self.__url = url

    @staticmethod
    def __build_url(url, params):
        return url + '?' + urlencode(params)

    def send_to_server(self, data, additional_params={}):
        for car_data in data:
            import_url = self.__build_url(self.__url, {**car_data, **additional_params})
            print('sending request to url: ' + import_url)
            urlopen(import_url)
