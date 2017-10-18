'''
In this assignment you will write a Python program that expands on
http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the
HTML from the data files below, extract the href = values from the anchor tags,
scan for a tag that is in a particular position relative to the first name in
the list, follow that link and repeat the process a number of times and report
the last name you find.

We provide two files for this assignment. One is a sample file where we give you
the name for your testing and the other is the actual data you need to process
for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this
process 4 times. The answer is the last name that you retrieve.
Sequence of names: Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Rebecca.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat
this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: A

+---------------------------Sample execution---------------------------+
|$ python3 solution.py                                                 |
|Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html         |
|Enter count: 4                                                        |
|Enter position: 3                                                     |
|Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html        |
|Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html    |
|Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html      |
|Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html        |
|Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html        |
+----------------------------------------------------------------------+

The answer to the assignment for this execution is "Anayah".
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean; fl -> file; t -> tuples
# l -> list; d -> dictionary; sock -> socket; byte -> bytes; bs -> BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def followLink(sUrl = 'http://py4e-data.dr-chuck.net/known_by_Rebecca.html', iCount = 0):
    # Ignore SSL certificate errors
    sslContext = ssl.create_default_context()
    sslContext.check_hostname = False
    sslContext.verify_mode = ssl.CERT_NONE

    byteHtml = urlopen(sUrl, context = sslContext).read()
    bsSoup = BeautifulSoup(byteHtml, "html.parser")
    bsElementResultSet = bsSoup('a')
    lContents = [(bsElementTag.contents[0], bsElementTag.get('href', None)) for bsElementTag in bsElementResultSet]
    tContentAndHref = lContents[intPosition]
    bsStrContent = tContentAndHref[0]
    bsStrHref = tContentAndHref[1]
    print('Retrieving:',bsStrHref,bsStrContent)
    if(iCount < intCount - 1):
        return(followLink(bsStrHref, iCount + 1))

stringUrl = input('Enter URL: ')
intCount = int(input('Enter count: '))
intPosition = int(input('Enter position: ')) - 1

try:
    followLink(stringUrl)
except:
    followLink()
