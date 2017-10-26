'''
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that
you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt

There are three ways that you might retrieve this web page and look at the
response headers:

1) Preferred: Modify the socket1.py (below of this text) program to retrieve the
above URL and print out the headers and data. Make sure to change the code to
retrieve the above URL - the values are different for each URL.
+------------------------------socket1.py------------------------------+
| import socket                                                        |
|                                                                      |
| mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           |
| mysock.connect(('data.pr4e.org', 80))                                |
| cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() |
| mysock.send(cmd)                                                     |
|                                                                      |
| while True:                                                          |
|     data = mysock.recv(512)                                          |
|     if (len(data) < 1):                                              |
|         break                                                        |
|     print(data.decode())                                             |
| mysock.close()                                                       |
+----------------------------------------------------------------------+
2) Open the URL in a web browser with a developer console or FireBug and
manually examine the headers that are returned.
3) Use the telnet program as shown in lecture to retrieve the headers and
content.
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean; fl -> file; t -> tuples
# l -> list; d -> dictionary; ; byte -> bytes;
# sock -> socket object;
import socket

sockSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sHost = 'data.pr4e.org'
iPort = 80
sockSocket.connect((sHost, iPort))
sRequestLine = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0'
byteCmd = (sRequestLine + '\r\n\r\n').encode()
sockSocket.send(byteCmd) # method send() to transmit the TCP message

while True:
    byteData = sockSocket.recv(512)
    if (len(byteData) < 1):
        break
    print(byteData.decode())

sockSocket.close()
