'''
Python provides two levels of access to network services. At a low level, you
can access the basic socket support in the underlying operating system, which
allows you to implement clients and servers for both connection-oriented and
connectionless protocols.

Python also has libraries that provide higher-level access to specific
application-level network protocols, such as FTP, HTTP, and so on.
(resource: https://www.tutorialspoint.com/python/python_networking.htm)

=====================================socket=====================================
A socket is one endpoint of a two-way communication link between two programs
running on the network. A socket is bound to a port number so that the TCP layer
can identify the application that data is destined to be sent to. An endpoint is
a combination of an IP address and a port number.

A socket is much like a file, except that a single socket provides a two-way
connection between two programs. You can both read from and write to the same
socket. If you write something to a socket, it is sent to the application at the
other end of the socket. If you read from the socket, you are given the data
which the other application has sent.

To create a socket, you must use the socket.socket() function available in
socket module, which has the general syntax −
+------------------------------------------------------------------+
| cSocket = socket.socket (socket_family, socket_type, protocol=0) |
+------------------------------------------------------------------+

The following code is like dialing a phone number; doesn't do anything else:

+----------------------------Example----------------------------+
| import socket                                                 |
| cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   |
| cSocket.connect(('data.pr4e.org', 80))                        |
+---------------------------------------------------------------+

Domain:
These constants represent the address (and protocol) families:
socket.AF_UNIX
socket.AF_INET: These sockets account for at least 99% of the sockets in use
socket.AF_INET6

Type:
socket.SOCK_STREAM: for connection-oriented protocols
socket.SOCK_DGRAM: for connectionless protocols
socket.SOCK_RAW
socket.SOCK_RDM
socket.SOCK_SEQPACKET

Protocol:
Typically zero, this may be used to identify a variant of a protocol within a
domain and type. This is usually left out, defaulting to 0.

Server Socket Methods:
cSocket.bind(): This method binds address (hostname, port number pair) to socket.
cSocket.listen(): This method sets up and start TCP listener.
cSocket.accept(): This passively accept TCP client connection, waiting until
                  connection arrives (blocking).

Client Socket Methods:
cSocket.connect(): This method actively initiates TCP server connection.

General Socket Methods:
cSocket.recv(): This method receives TCP message
cSocket.send(): This method transmits TCP message
cSocket.recvfrom(): This method receives UDP message
cSocket.sendto(): This method transmits UDP message
cSocket.close(): This method closes socket
socket.gethostname(): Returns the hostname.

'''
