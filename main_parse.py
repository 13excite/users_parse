from bs4 import BeautifulSoup
import re
from auth import get_url
import argparse
import os

URL = 'http://liga-znakomstv.ru/public/profile.php?profile='

my_cookie = 'dds'


def exception_index_list(lst, index):
    try:
        return lst[index]
    except:
        return "Empty"


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
    link_pattern = re.compile('(https:\/\/)?(www\.)?(vk\.com\/)(id\d|[a-zA-z][a-zA-Z0-9_.]{2,})|(t\.me)|(facebook)|(id\d)(@\w\w)')
    fake_link = re.compile('liga_znakomstv')
    empty_lst = []
    for item in lst:
        if item:
            if link_pattern.findall(item) and not fake_link.findall(item):
                empty_lst.append(item)
    return empty_lst


def create_html_table(user_list):
    name = exception_index_list(user_list, 0)
    age = exception_index_list(user_list, 1)
    birth_date = exception_index_list(user_list, 2)
    country = exception_index_list(user_list, 3)
    town = exception_index_list(user_list, 4)

    str_table = "<td>"+name+"</td><td>"+age+"</td><td>"+birth_date+"</td><td>"+country+"</td><td>"+town+"</td>"
    return  str_table


def file_writer(user_info_str, contacts_list, user_id, result_file):
    user_id = str(user_id)
    if len(contacts_list) > 1:
        contacts_string = ",".join(contacts_list)
    else:
        try:
            contacts_string = contacts_list[0]
        except:
            contacts_string = 'Not found'

    full_string = "<tr>" + user_info_str + "<td>" + contacts_string + "</td><td>" + user_id +"</td></tr>"
    with open(result_file, 'a') as f:
        f.write(full_string.encode('utf8') + "\n")
      #  pass
        # somebody write to file
    #return full_string


def main():
    profile_start = 3500
    profile_finish = 4834
    parser = argparse.ArgumentParser(description='usage %s -s 100 -e 1100 -o out_result.html ' % os.path.basename(__file__))
    parser.add_argument('-s', '--start', type=int, help='start page id', required=True)
    parser.add_argument('-e', '--end', type=int, help='end page id', required=True)
    parser.add_argument('-o', '--out', type=str, help='path to out html file', required=True)
    args = parser.parse_args()

    for user_id in range(args.start, args.end):
        valid_url = URL + str(user_id)
        html_doc = get_url(valid_url, my_cookie)
        user_info_tags = tags_getter(html_doc, 'dd')
        contacs = get_contacts(html_doc)

        file_writer(create_html_table(user_info_tags), parsing_cuntacts_urls(contacs), user_id, args.out)


if __name__ == '__main__':
    main()


