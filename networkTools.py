import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


def request_via_network(url):
    if url.startswith('http') or url.startswith('https'):
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            time.sleep(1)
            data = res.text
            return data
        else:
            return ''
    else:
        return ''
