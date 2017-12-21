from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile=4805'
my_cookie = 'fisdjfdjf'

def re_parse(tag_list, re_pattern):
    finish_list = []
    p = re.compile(re_pattern)
    for elm in tag_list:
        if p.findall(elm):
            finish_list.append(elm)
    return finish_list

def tags_getter(html, tag):
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = []
    for t in soup.find_all(tag):
        try:
            tag_list.append(t.text)
        except:
            print 'Not find data in this tag'
    return tag_list


def get_contacts(html):
    soup = BeautifulSoup(html, 'html.parser')
    my_link = []
    for link in soup.find_all('a'):
        my_link.append(link.get('href'))
    return my_link

def a_tags_parser(list_urls):
    pass


if __name__ == '__main__':
    html_doc = get_url(URL, my_cookie)

    user_info_tags = tags_getter(html_doc, 'dd')
    contacs = get_contacts(html_doc)
    print contacs
    for elm in user_info_tags:
        print "<p>%s</p>" % elm

