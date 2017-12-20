#!/usr/bin/python

import requests
import socket
import sys
import logging


OK_RESPONSE = 200

def is_ipv4(s):
    """
    Checked ipv4
    """
    return ':' not in s

#var for script dns cache
dns_cache = {}

def add_custom_dns(domain, port, ip):
    key = (domain, port)
    if is_ipv4:
        value = (socket.AF_INET, 0, 0,  '', (ip, port))
    else:
        value = (socket.AF_INET6, 0, 0, '', (ip, port, 0, 0))
    dns_cache[key] = [value]

prv_getaddrinfo = socket.getaddrinfo

def new_getaddrinfo(*args):
    try:
        return dns_cache[args[:2]]
    except:
        return prv_getaddrinfo(*args)

socket.getaddrinfo = new_getaddrinfo

hb_dic = {'HB1' : '217..1..1', 'HB2' : '217.1.1.1', 'HB3' : '217.1.1.1', 'HB4' : '217.1.1.1' }

try:
    import http.client as http_client
except ImportError:
        # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug
# output.
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.INFO)
requests_log.propagate = True

for hotbox_name,hotbox_ip in hb_dic.iteritems():

    add_custom_dns('hb.bizmrg.com', 80, hotbox_ip)
    try:
        res = requests.get('https://hb.b.ng', timeout=(3,2))
    except requests.exceptions.ConnectTimeout:
        print "Concetion timeout %s on hb.bizmrg.com" % (hotbox_name)
        sys.exit(2)

    res = requests.get('https://hb.w.com/hb.png')
    print res.text
    response_code = res.status_code
    print response_code
    if response_code != OK_RESPONSE:
        print "ALARM %s status code %s CALL!!!!!" % (hotbox_name, response_code)
        sys.exit(2)
