import requests


theurl = "http://liga-znakomstv.ru/public/profile.php?profile=4144"
username = "test"
passwd = "test1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Cookie': 'blabla',
      }
r = requests.get(theurl)
with open('test.html', 'w') as file:
    file.write(r.text.encode('UTF-8'))



