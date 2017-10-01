import requests


theurl = "http://liga-znakomstv.ru/public/profile.php?profile=4144"



headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'X-Compress': 'null',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://liga-znakomstv.ru/',
    'Cookie': 'blabla',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
      }
r = requests.get(theurl, headers=headers)
with open('test.html', 'w') as file:
    file.write(r.text.encode('UTF-8'))



