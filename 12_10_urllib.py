'''
=================================urllib.request=================================
The module urllib.request is a Python module for fetching URLs.
It offers a very simple interface, in the form of the urlopen function.
This is capable of fetching URLs using a variety of different protocols.
Let’s take a look at a simple way to fetch the contents of a specific URL:
+----------------------------Example-----------------------------+
|import urllib.request                                           |
|# Open the connection to the URL                                |
|response = urllib.request.urlopen('http://www.python.org')      |
|# used the urlconnection to read all the data into a variable   |
|html = response.read().decode().split('\n')                     |
|# go through all the lines in the variable (content of the URL) |
|For linein html:                                                |
|    print(line)                                                 |
|# Like a file...                                                |
+----------------------------------------------------------------+

There are 2 handy functions that can be used with the reponse object returned
when we call urlopen(). They are info() and geturl()
Let’s take a look at an example of how to use them:
+-----------------------------------Example------------------------------------+
|import urllib.request                                                         |
|# Open the connection to the URL                                              |
|response = urllib.request.urlopen('http://www.python.org')                    |
|# use the info() function in order to obtain information about the urlfetched.|
|print (response.info())                                                       |
|# use the geturl() function to get the actual URL retrieved                   |
|print (response.geturl())                                                     |
+------------------------------------------------------------------------------+

By using the info() function you can also get to specific headers in the
returned URL
+-----------------------------------Example------------------------------------+
|import urllib.request                                                         |
|# Open the connection to the URL                                              |
|response = urllib.request.urlopen('http://www.python.org')                    |
|# use the info() function in order to obtain information about the urlfetched.|
|headers = response.info()                                                     |
|# use the geturl() function to get the actual URL retrieved                   |
|print (headers["Date"])                                                       |
|print (headers["Content-Type"])                                               |
+------------------------------------------------------------------------------+

'''
