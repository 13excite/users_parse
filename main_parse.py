from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile=4805'
HTML_FILE = './test1.html'
my_cookie = 'fff'

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

def parsing_cuntacts_urls(lst):
    link_pattern = re.compile('(https:\/\/)?(www\.)?(vk\.com\/)(id\d|[a-zA-z][a-zA-Z0-9_.]{2,})')
    empty_lst = []
    for item in lst:
        if link_pattern.findall(item):
            empty_lst.append(item)
    return empty_lst


def create_html_table(user_list):
    name = user_list[0]
    age = user_list[1]
    birth_date = user_list[2]
    country = user_list[3]
    town = user_list[4]

    str_table = "<td>"+name+"</td><td>"+age+"</td><td>"+birth_date+"</td><td>"+country+"</td><td>"+town+"</td>"
    return  str_table

def file_writer(user_info_tags_str, contacts_list):
    contacts_len = len(contacts_list)
    if contacts_len < 2:
        full_string = user_info_tags + "<td>"+contacts_list[0]+"</td>"
    else:
        pass
    with open(HTML_FILE, 'a') as f:
        pass
        # somebody write to file




if __name__ == '__main__':
    html_doc = get_url(URL, my_cookie)

    user_info_tags = tags_getter(html_doc, 'dd')
    contacs = get_contacts(html_doc)
    #print contacs
    #for elm in user_info_tags:
     #   print "<p>%s</p>" % elm
    print create_html_table(user_info_tags)

