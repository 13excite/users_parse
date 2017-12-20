from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile=4798'
my_cookie = 'ddd'

def re_parse(tag_list, re_pattern):
    finish_list = []
    p = re.compile(re_pattern)
    for elm in tag_list:
        if p.findall(elm):
            finish_list.append(elm)
    return finish_list

def first_parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = []
    for tag in soup.find_all('dd'):
        try:
            tag_list.append(tag)
        except:
            tag_list.append(tag)
    return tag_list

def get_contacts(html_tags):
    pass

def generic_html_table(name, contacts, age, sex):
    pass


if __name__ == '__main__':
    html_doc = first_parse(get_url(URL, my_cookie))
    print html_doc

