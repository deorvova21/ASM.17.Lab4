import urllib


class ModelSender:
    def __init__(self, url, common_params):
        self.url = url
        self.common_params = common_params

    def send(self, agency):
        for model in agency:
            model_params = model.get_params()
            self.request(model_params)
            print(str(model) + ' sent!')
        print('Done!')

    def request(self, model_params):
        request = self.url + '?' + urllib.parse.urlencode(self.common_params) + \
                  '&' + urllib.parse.urlencode(model_params)
        urllib.request.urlopen(request)
