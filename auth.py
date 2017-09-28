import urllib2
import sys
import base64
import urlparse
import re
#from bs4 import BeautifulSoup


theurl = "http://liga-znakomstv.ru/public/index.php"
username = "test"
passwd = "test1"

req = urllib2.Request
try:
    handle = urllib2.urlopen(req)
except IOError, e:
    pass
else:
    # If we don't fail then the page isn't protected
    print "This page isn't protected by authentication."
    sys.exit(1)
if not hasattr(e, 'code') or e.code != 401:
    # we got an error - but not a 401 error
    print "This page isn't protected by authentication."
    print 'But we failed for another reason.'
    sys.exit(1)

authline = e.headers['www-authenticate']
# this gets the www-authenticate line from the headers
    # which has the authentication scheme and realm in it


