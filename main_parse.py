from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile='
HTML_FILE = './test1.html'
my_cookie = 'ss'

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
    link_pattern = re.compile('(https:\/\/)?(www\.)?(vk\.com\/)(id\d|[a-zA-z][a-zA-Z0-9_.]{2,})|(t\.me)|(facebook)|(id\d)')
    fake_link = re.compile('liga_znakomstv')
    empty_lst = []
    for item in lst:
        if item:
            if link_pattern.findall(item) and not fake_link.findall(item):
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

def file_writer(user_info_str, contacts_list):
    if len(contacts_list) > 1:
        contacts_string = ",".join(contacts_list)
    else:
        try:
            contacts_string = contacts_list[0]
        except:
            contacts_string = 'Not found'

    full_string = user_info_str + "<td>" + contacts_string + "</td>"
    with open(HTML_FILE, 'a') as f:
        f.write(full_string.encode('utf8') + "\n")
      #  pass
        # somebody write to file
    #return full_string


if __name__ == '__main__':
    profile_start = 4518
    profile_finish = 4519

    for user_id in range(profile_start,profile_finish):
        valid_url = URL + str(user_id)
        html_doc = get_url(valid_url, my_cookie)
        user_info_tags = tags_getter(html_doc, 'dd')
        contacs = get_contacts(html_doc)

        file_writer(create_html_table(user_info_tags), parsing_cuntacts_urls(contacs))

