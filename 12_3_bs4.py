'''
Using beautifulsoup write a program that does the following:
Open the URL www.meteomedia.com
Find how many <a> tags are there in the html code
Print all href links
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean; fl -> file; t -> tuples
# l -> list; d -> dictionary; ; byte -> bytes;
# sock -> socket object; bs -> BeautifulSoup object

import urllib.request
from bs4 import BeautifulSoup

byteHtml = urllib.request.urlopen('http://www.httpbin.org').read()
bsSoup = BeautifulSoup(byteHtml, "html.parser")
bsElementResultSet = bsSoup('a')

for bsElementTag in bsElementResultSet:
    sHref = bsElementTag.get('href', None)
    lHrefContents = bsElementTag.contents
    dAttrs = bsElementTag.attrs
    print('TAG:', bsElementTag)
    print('URL:', sHref)
    print('Contents:', lHrefContents[0])
    print('Attrs:', dAttrs)
