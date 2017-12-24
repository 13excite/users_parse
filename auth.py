import requests
from fake_useragent import UserAgent

def get_url(url, cookie):
  #  ua = UserAgent()
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'Upgrade-Insecure-Requests': '1',
        'X-Compress': 'null',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://liga-znakomstv.ru/',
        'Cookie': cookie,
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
          }
    try:
        r = requests.get(url, headers=headers)
    except:
        print 'request failed'
    return r.text



