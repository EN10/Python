from concurrent.futures import ThreadPoolExecutor
import requests

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def make_req(url):
    req = requests.get(url,timeout=10)
    print(url + ' : ' + str(req.status_code))

with ThreadPoolExecutor(max_workers=8) as executor:
    for _ in executor.map(make_req, URLS):
        pass
