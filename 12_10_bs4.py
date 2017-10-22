'''
=================================beautifulsoup==================================
The module beautifulsoup allows us to navigate html pages in a very convenient
way. We do not have to program the details of finding specific tags and extract
content, beautifulsoup does that for us.

Let’s take a look at a trivial example of using beautifulsoup to extract all <a>
tags from the html of a web page.
+------------------Example-------------------+
|import urllib.request                       |
|from bs4 import BeautifulSoup               |
|url= 'http://httpbin.org'                   |
|response = urllib.request.urlopen(url)      |
|html = response.read()                      |
|soup = BeautifulSoup(html, "html.parser")   |
|a_tags= soup('a')                           |
|for rows in a_tags:                         |
|    print(rows)                             |
+--------------------------------------------+

Let’s explore couple of other features of beautifulsoup. Lets get a specific
element inside a tag and the content of the tag (its value).
+-------------------Example--------------------+
|import urllib.request                         |
|from bs4 import BeautifulSoup                 |
|url= 'http://httpbin.org'                     |
|response = urllib.request.urlopen(url)        |
|html = response.read()                        |
|soup = BeautifulSoup(html, "html.parser")     |
|a_tags= soup('a')                             |
|for rows in a_tags:                           |
|    print(rows.get('href'))                   |
|    print(rows.contents)                      |
+----------------------------------------------+

Another helpful method, findAll():
+-------------------Example--------------------+
|import urllib.request                         |
|from bs4 import BeautifulSoup                 |
|url= 'http://httpbin.org'                     |
|response = urllib.request.urlopen(url)        |
|html = response.read()                        |
|soup = BeautifulSoup(html, "html.parser")     |
|#trying findall()                             |
|a_tags= soup.findAll('a')                     |
|for rows in a_tags:                           |
|    print(rows.get('href'))                   |
|    print(rows.contents)                      |
+----------------------------------------------+

**************************About Characters and Strings**************************
ASCII:
We refer to "8 bits of memory as a "byte" of memory – (i.e. my disk drive
contains 3 Terabytes of memory) The ord() function tells us the numeric value of
a simple ASCII character:

>>> print(ord('H'))
72
>>> print(ord('e'))
101
>>> print(ord('\n'))
10
>>>

Multi-Byte Characters:
To represent the wide range of characters computers must handle we represent
characters with more than one byte:
* UTF-16 – Fixed length - Two bytes
* UTF-32 – Fixed Length - Four Bytes
* UTF-8 – 1-4 bytes
 - Upwards compatible with ASCII
 - Automatic detection between ASCII and UTF-8
 - UTF-8 is recommended practice for encoding    data to be exchanged between systems

Python 2 versus Python 3

  Python 2.7.10           Python 3.5.1
------------------      ------------------
>>> x = b'abc'          >>> x = b'abc'
>>> type(x)             >>> type(x)
<type 'str'>            <class 'bytes'>
>>> x = '이광춘'         >>> x = '이광춘'
>>> type(x)             >>> type(x)
<type 'str'>            <class 'str'>
>>> x = u'이광춘'        >>> x = u'이광춘'
>>> type(x)             >>> type(x)
<type 'unicode'>        <class 'str'>

* In Python 3, all strings internally are UNICODE
* Working with string variables in Python programs and reading data from files
  usually "just works"
* When we talk to a network resource using sockets or talk to a database we have
  to encode and decode data (usually to UTF-8)

Python Strings to Bytes:
* When we talk to an external resource like a network socket we send bytes, so we
  need to encode Python 3 strings into a given character encoding
* When we read data from an external resource, we must decode it based on the
  character set so it is properly represented in Python 3 as a string

  while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)
'''
