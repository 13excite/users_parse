from bs4 import BeautifulSoup
import re
from auth import get_url

URL = ''
my_cookie = ''

def re_parse(tag_list, re_pattern):
    finish_list = []
    p = re.compile(re_pattern)
    for elm in tag_list:
        if p.findall(elm):
            finish_list.append(elm)
    return finish_list

def first_parse(html_doc):
    """
    find all 'a' tags in html doc
     and return tag's list
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    finish_dict = dict()
    a_tag_list = []

    for tag in soup.find_all('a'):
        a_tag_list.append(tag.get('href'))
    return finish_dict

def get_contacts(html_tags):
    pass

def generic_html_table(name, contacts, age, sex):
    pass


if __name__ == '__main__':
    html_doc = get_url(URL, my_cookie)

