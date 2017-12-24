from bs4 import BeautifulSoup
import re
from auth import get_url
import json

URL = 'http://liga-znakomstv.ru/public/profile.php?profile=4805'
HTML_FILE = './test1.html'
my_cookie = 'dd'

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
    link_pattern = re.compile('(https:\/\/)?(www\.)?(vk\.com\/)(id\d|[a-zA-z][a-zA-Z0-9_.]{2,})|(t\.me)|(facebook)')
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

def file_writer(user_info_tags_str, contacts_list):
    if len(contacts_list) > 1:
        contacts_string = ",".join(contacts_list)
        print 'AAAA'
        print contacts_string
        print type(contacts_string)
    else:
        contacts_string = contacts_list[0]
        print 'BBBBB'
        print contacts_string
        print type(contacts_string)

    print user_info_tags_str
    print type(user_info_tags_str)
    #full_string = user_info_tags.decode('utf8') + "<td>".decode('utf8') + contacts_string + "</td>".decode('utf8')
    #with open(HTML_FILE, 'a') as f:
      #  pass
        # somebody write to file
    #return full_string




if __name__ == '__main__':
    html_doc = get_url(URL, my_cookie)

    user_info_tags = tags_getter(html_doc, 'dd')
    contacs = get_contacts(html_doc)

    #print type(format(parsing_cuntacts_urls(contacs)[0]))
    #print contacs
    #for elm in user_info_tags:
     #   print "<p>%s</p>" % elm
    #print create_html_table(user_info_tags)

    print file_writer(create_html_table(user_info_tags), parsing_cuntacts_urls(contacs))

