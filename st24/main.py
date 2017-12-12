from .Comrade import Comrade
from .PartyElite import PartyElite
import pickle
import re
import urllib.request as rq
import urllib.parse as prs

MY_NUMBER = 24
PATH = 'st24/uploading_data.pkl'


def main():
    global data
    with open(PATH, 'rb') as f:
        data = pickle.load(f)

    response = rq.urlopen('http://localhost:81/cgi-bin/lab3.py')
    html_data = str(response.read())

    for item in data[0]:
        params = {
            'fullname': item._name,
            'party_name': item._party_name,
            'id': item.id,
            'student':re.search(r'student=(\d+)\">\[' + str(MY_NUMBER) + '\]', html_data).group(1)
        }
        if (type(item) is Comrade):
            params['action'] = 'add_comrade'
        else:
            params['action'] = 'add_party_elite'
            params['position'] =  item._position
        request_url = 'http://localhost:81/cgi-bin/lab3.py' + '?' + prs.urlencode(params)
        rq.urlopen(request_url)

if __name__ == "__main__":
    main()
