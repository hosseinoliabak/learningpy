'''
Using beautifulsoup write a program that does the following:
Open the URL www.meteomedia.com
Find how many <a> tags are there in the html code
Print all href links
'''
import urllib.request
from bs4 import BeautifulSoup
httpResponse = urllib.request.urlopen('http://httpbin.org')
bHtml = httpResponse.read()
bsSoup = BeautifulSoup(bHtml, "html.parser")
bsElement_a = bsSoup('a')
for rows in bsElement_a:
    sHref = rows.get('href')
    lHrefContents = rows.contents
    print(sHref)
    print(lHrefContents)
