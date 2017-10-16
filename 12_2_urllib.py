"""
Urllib (for this exercise you won't be using beautifulsoup; not yet)

Fetch (don't print) the html content from the page www.bbc.com/news (hhtp)
Can you tell how many characters are there in the html page?
Can you tell how many lines?
Print the first and last line of the html code.
Use the info() method to print all the headers
Can you tell how many times the string "BBC" is found in the code?
"""
import urllib.request, re
iCount = 0
lLine = list()
httpResponse = urllib.request.urlopen('http://www.bbc.com/news')
sHtml = httpResponse.read().decode()
lHtml = sHtml.split('\n')
for sLine in lHtml:
    iCount += 1
    lLine.append(sLine)
lBBC = re.findall(r'\sBBC\s',sHtml)
print ('-------------------------HTTP header-------------------------')
print(httpResponse.info())
print ('-------------------------------------------------------------')
print('There are', iCount, 'lines in this page!')
print(' - First line:', lLine[0])
print(' - Last line:', lLine[-1])
print('There are', len(sHtml), 'characters in this page!' )
print('There are', len(lBBC), 'occurrence of the word BBC in the HTML code.')
