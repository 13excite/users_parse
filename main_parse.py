from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile=4798'
my_cookie = 'ddddd'

def re_parse(tag_list, re_pattern):
    finish_list = []
    p = re.compile(re_pattern)
    for elm in tag_list:
        if p.findall(elm):
            finish_list.append(elm)
    return finish_list

def get_main_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = []
    for tag in soup.find_all('dd'):
        try:
            tag_list.append(tag.text)
        except:
            print 'Not find users info on page'
    return tag_list

def get_contacts(html_tags):
    pass

def generic_html_table(name, contacts, age, sex):
    pass


if __name__ == '__main__':
    html_doc = get_main_info(get_url(URL, my_cookie))
    for elm in html_doc:
        print "<p>%s</p>" % elm

