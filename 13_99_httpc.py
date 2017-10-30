'''
           Concordia University
           COMP6461 – Fall 2017
   Data Communications & Computer Networks
            Lab Assignment # 1

Introduction
In this assignment, you will implement a simple HTTP client application and
experiment it in real HTTP Servers (web servers). Before starting on this
assignment, it is strongly recommended that you read the provided programming
samples and review the associated course materials.

Outline
The following is a summary of the main tasks of the Assignment:
1. Study HTTP network protocol specifications.
2. Build your own HTTP client library.
3. Program your HTTP client application (curl command).
4. (optional) Implement more HTTP protocol specifications.
5. (optional) Enhance the functionalities of the HTTP client.

Objective
The goal of this Lab is to have your fist steps in implementing network protocol
from its technical specifications. Generally, the specifications of network
protocol (for example FTP for file transfer and NTP for time synchronization)
are provided by standardization organizations like IETF (http://www.ietf.org).

(A protocol is a system of rules that allow two or more entities of a
communications system to transmit information via any kind of variation of a
physical quantity. These are the rules or standard that defines the syntax,
semantics and synchronization of communication and possible error recovery
methods. Protocols may be implemented by hardware, software, or a combination of
both. [1])

Network protocols standards are used for various purposes and different
OSI - TCP/IP models layers. In the context of this Lab, we focus on implementing
as subset HTTP network protocol specifications on top of the transport layer,
TCP/UDP of OSI, TCP/IP models respectively.

(The Hypertext Transfer Protocol (HTTP) is an application protocol for
distributed, collaborative, hypermedia information systems. HTTP is the
foundation of data communication for the World Wide Web. [2])

For this purpose, you are requested to implement the basic functionalities of
cURL command line, the functionalities that are related to HTTP protocol.

(cURL is a computer software project providing a library and command-line tool
for transferring data using various protocols. The cURL project produces two
products, libcurl and cURL. It was first released in 1997. [3])

(cURL is an open source command line tool and library for transferring data with
URL syntax, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS,
LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMTP, SMTPS, Telnet and
TFTP. curl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP
form based upload, proxies, HTTP/2, cookies, user+password authentication
(Basic, Plain, Digest, CRAM-MD5, NTLM, Negotiate and Kerberos), file transfer
resume, proxy tunneling and more. [4])

Similarly to the cURL project, the requested implementation in this Lab need to
have a network protocol software library and the command line application.
Therefore, the main tasks of this Lab are the following:
1. Implementing your own HTTP client library using TCP Socket directly. Only a
subset of HTTP protocol features are requested. Specifically, you need to
implement GET and HTTP POST requests.

2. Leverage the developed HTTP client library to develop a command-line
application similar to the cURL one. However, your version needs only to have a
basic functionalities with limited options such as the POST, GET, and verbose
option.

Study HTTP Protocol
In this step, you are requested to have an overview of HTTP protocol.
Specifically, you should have a detailed understanding of The HTTP GET request
and POST response. HTTP protocol has multiple versions, 1.0, 1.1, 2.0, which you
can consider them references for you implementation (Only versions >= 1.0).
However, we urge you to use HTTP version 1.0 due to its simplicity and ease to
implement.

You can find the complete specifications of HTTP protocol version 1.0 at the
following link (http://www.w3.org/Protocols/HTTP/1.0/spec.html). However, we
believe that the best way to learn is by doing; meaning, experimenting sending
requests and receiving responses using the telnet command line.

Telnet is an application layer protocol used on the Internet or local area
networks to provide a bidirectional interactive text-oriented communication
facility using a virtual terminal connection. User data is interspersed in-band
with Telnet control information in an 8-bit byte oriented data connection over
the Transmission Control Protocol (TCP). Telnet was developed in 1969 beginning
with RFC 15, extended in RFC 854, and standardized as Internet Engineering Task
Force (IETF) Internet Standard STD 8, one of the first Internet standards. [5]

Following example depict how to telnet command line to send a simple HTTP GET
Request to http://httpbin.org/status/418 webpage.
+------------------------------------------------------+
|> telnet httpbin.org 80                               |
|                                                      |
|GET /status/418 HTTP/1.0                              |
|Host: httpbin.org                                     |
|                                                      |
|HTTP/1.1 418 I'M A TEAPOT                             |
|Server: nginx                                         |
|Date: Sat, 29 Jul 2017 21:58:24 GMT                   |
|Content-Length: 135                                   |
|Connection: close                                     |
|Access-Control-Allow-Origin: *                        |
|x-more-info: http://tools.ietf.org/html/rfc2324       |
|Access-Control-Allow-Credentials: true                |
|                                                      |
|    -=[ teapot ]=-                                    |
|                                                      |
|       _...._                                         |
|     .'  _ _ `.                                       |
|    | ."` ^ `". _,                                    |
|    \_;`"---"`|//                                     |
|      |       ;/                                      |
|      \_     _/                                       |
|        `"""`                                         |
|Connection closed by foreign host.                    |
+------------------------------------------------------+

To reproduce the example, your should follow the following steps:
1. Launch your terminal/command console. Most operating systems have the telnet
command line installed. If this is not the case on your version, you need to
install it.
2. In the terminal type telnet httpbin.org 80, where httpbin.org is the HTTP
server and '80' is the standard HTTP TCP port.
3. Once telnet connected, type GET /status/418 HTTP/1.0, then press Enter in the
keyboard.
4. Afterward, type Host: httpbin.org then two times Enter to send the request to
httpbin.org HTTP Server.
You should receive the response depicted in the output sample. Similarly, you
can explore HTTP protocol operations without the need to program.

HTTP Client Library Implementation
After getting a deeper understanding of the flow of HTTP GET and POST
operations, you are requested to implement your HTTP client using TCP Sockets.
The programming library implements only a small subset of HTTP specifications.
In other words, we expect that your HTTP library supports the following features:
1. GET operation
2. POST operation
3. Query parameters
4. Request headers
5. Body of the request
You can refer to HTTP protocol reference (http://www.w3.org/Protocols/HTTP/1.0/spec.html)
for more information about these features. You can start your implementation by
leveraging the provided samplesfor HTTP-ECHO (https://tools.ietf.org/html/rfc862)
and HTTP-TIME (https://tools.ietf.org/html/rfc868) protocols at the example
directory.

To this end, you should build your testing demos for the HTTP client library in
order to demonstrate it.

cURL-like Command Line Implementation
At this stage, you are ready to build a simple HTTP client using your library.
In this task, you are requested to implement cURL command line with basic
functionalities.
For this purpose, you need to experiment with cURL command line in your
preferred terminal in order to know its basic options. You should notice that
our focus is on the options related to HTTP protocol since cURL support many
network protocols as described earlier.

The implemented client should be named httpc (the name of the produced executable).
The following presents the options of your final command line.
+----------------------------------------------------------------+
|httpc (get|post) [-v] (-h "k:v")* [-d inline-data] [-f file] URL|
+----------------------------------------------------------------+
In the following, we describe the purpose of the expected httpc command options:
1. Option -v enables a verbose output from the command-line. Verbosity could be
useful for testing and debugging stages where you need more information to do so.
You define the format of the output. However, You are expected to print all the
status, and its headers, then the contents of the response.
2. URL determines the targeted HTTP server. It could contain parameters of the
HTTP operation. For example, the URL 'https://www.google.ca/?q=hello+world'
includes the parameter q with "hello world" value.
3. To pass the headers value to your HTTP operation, you could use -h option.
The latter means setting the header of the request in the format "key: value."
Notice that; you can have multiple headers by having the -h option before each
header parameter.
4. -d gives the user the possibility to associate the body of the HTTP Request
with the inline data, meaning a set of characters for standard input.
5. Similarly to -d, -f associate the body of the HTTP Request with the data from
a given file.
6. get/post options are used to execute GET/POST requests respectively. post
should have either -d or -f but not both. However, get option should not used
with the options -d or -f.

Detailed Usage

+------------------------------General-----------------------------+
|httpc help                                                        |
|httpc is a curl-like application but supports HTTP protocol only. |
|Usage:                                                            |
|httpc command [arguments]                                         |
|The commands are:                                                 |
|get executes a HTTP GET request and prints the response.          |
|post executes a HTTP POST request and prints the response.        |
|help prints this screen.                                          |
|Use "httpc help [command]" for more information about a command.  |
+------------------------------------------------------------------+
+----------------------------------Get Usage----------------------------------+
|httpc help get                                                               |
|usage: httpc get [-v] [-h key:value] URL                                     |
|Get executes a HTTP GET request for a given URL.                             |
|-v Prints the detail of the response such as protocol, status, and headers.  |
|-h key:value Associates headers to HTTP Request with the format 'key:value'. |
+-----------------------------------------------------------------------------+
+-----------------------------------Post Usage-----------------------------------+
|httpc help post                                                                 |
|usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL            |
|Post executes a HTTP POST request for a given URL with inline data or from file.|
|-v Prints the detail of the response such as protocol, status, and headers.     |
|-h key:value Associates headers to HTTP Request with the format 'key:value'.    |
|-d string Associates an inline data to the body HTTP POST request.              |
|-f file Associates the content of a file to the body HTTP POST request.         |
|                                                                                |
|Either [-d] or [-f] can be used but not both.                                   |
+--------------------------------------------------------------------------------+
Example: Get with query parameters
+-----------------------------Examples-----------------------------+
|httpc get 'http://httpbin.org/get?course=networking&assignment=1' |
+------------------------------------------------------------------+
+-------------------------------Output-------------------------------+
|{                                                                   |
|  "args": {                                                         |
|    "assignment": "1",                                              |
|    "course": "networking"                                          |
|  },                                                                |
|  "headers": {                                                      |
|    "Host": "httpbin.org",                                          |
|    "User-Agent": "Concordia-HTTP/1.0"                              |
|  },                                                                |
|  "url": "http://httpbin.org/get?course=networking&assignment=1"    |
|}                                                                   |
+--------------------------------------------------------------------+

+-----------------------Get with verbose option-----------------------+
|httpc get -v 'http://httpbin.org/get?course=networking&assignment=1' |
+---------------------------------------------------------------------+
+-------------------------------Output-------------------------------+
|HTTP/1.1 200 OK                                                     |
|Server: nginx                                                       |
|Date: Fri, 1 Sep 2017 14:52:12 GMT                                  |
|Content-Type: application/json                                      |
|Content-Length: 255                                                 |
|Connection: close                                                   |
|Access-Control-Allow-Origin: *                                      |
|Access-Control-Allow-Credentials: true                              |
|{                                                                   |
|  "args": {                                                         |
|    "assignment": "1",                                              |
|    "course": "networking"                                          |
|  },                                                                |
|  "headers": {                                                      |
|    "Host": "httpbin.org",                                          |
|    "User-Agent": "Concordia-HTTP/1.0"                              |
|  },                                                                |
|  "url": "http://httpbin.org/get?course=networking&assignment=1"    |
|}                                                                   |
+--------------------------------------------------------------------+

+-----------------------Post with inline data------------------------+
|httpc post -h Content-Type:application/json --d '{"Assignment": 1}' |
|http://httpbin.org/post                                             |
+--------------------------------------------------------------------+
+--------------------Output--------------------+
|{                                             |
|  "args": {},                                 |
|  "data": "{\"Assignment\": 1}",              |
|  "files": {},                                |
|  "form": {},                                 |
|  "headers": {                                |
|    "Content-Length": "17",                   |
|    "Content-Type": "application/json",       |
|    "Host": "httpbin.org",                    |
|    "User-Agent": "Concordia-HTTP/1.0"        |
|  },                                          |
|  "json": {                                   |
|    "Assignment": 1                           |
|  },                                          |
|  "url": "http://httpbin.org/post"            |
|}                                             |
+----------------------------------------------+

Optional Tasks (Bonus Marks)
If you have successfully completed the material above, congratulations! The
reason behind such congratulations is that you now understand the implementation
of an HTTP client and network protocols in general. For the rest of this lab
exercise, we have included the following optional tasks. These optional tasks
will help you gain a deeper understanding of the material, and if you can do so,
we encourage you to complete them as well.


Enhance Your HTTP Client library
In the current HTTP library, you already implemented the necessary HTTP
specifications, GET and POST. In this optional task, you need to implement one
new specification of HTTP protocol that is related to the client side. For
example, you could develop one of the Redirection specifications. The latter
allow your HTTP client to follow the first request with another one to new URL
if the client receives a redirection code (numbers starts with 3xx). This option
is useful when the HTTP client deal with temporally or parental moved URLs.
Notice, you are free to choose which HTTP specification to implement in your
HTTP library. After selecting the specification, you should consult with the Lab
Instructor before starting their implementations.

Update The cURL Command line
Accordingly, you could add the newly implemented HTTP specifications in your
HTTP library to the httpc command line. To do that, you need to create a new
option that allows the user the access the newly implemented specification. In
addition, you are requested to add the option –o filename, which allow the HTTP
client to write the body of the response to the specified file instead of the
console. For example, the following will write the response to hello.txt:
+-----------------------------------------------------------------------------+
|httpc -v 'http://httpbin.org/get?course=networking&assignment=1' -o hello.txt|
+-----------------------------------------------------------------------------+
Testing
You should be able to test your application with any HTTP server.
The httpbin.org provides an excellent service for you to check your command-line.
You can write a small utility that calls both your httpc and cURL against the
same URL with the same parameters and then compare the responses.

References
[1] Communications Protocol. https://en.wikipedia.org/wiki/Communications_protocol.
[2] Hypertext Transfer Protocol. https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol.
Comp6461 – Fall 2017 - Lab Assignment # 1 Page 11
[3] cURL: https://en.wikipedia.org/wiki/CURL.
[4] cURL: https://curl.haxx.se.
[5] Telnet: https://en.wikipedia.org/wiki/Telnet.
'''
import argparse, urllib.request, urllib.parse, json, re

def getArguments():

    # Assign help to the function
    '''This function parses and returns arguments passed in'''

    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        prog='httpc.py',
        description='httpc is a curl-like application but supports HTTP protocol only.')

    ##### Make a verbose help #####
    # parser.add_argument('help', default = None, nargs='?')
    # subHelp = parser.add_subparsers()
    # getHelp = subHelp.add_parser('get', help='HELP GET')
    # postHelp = subHelp.add_parser('post', help='HELP POST')

    # Add positional arguments get/post
    methodHelp = '''get/post options are used to execute GET/POST requests
    respectively. post should have either -d or -f but not both. However, get
    option should not used with the options -d or -f.'''
    lChoices = ['get', 'post']
    parser.add_argument('method', choices=lChoices, help=methodHelp, default = 'get', nargs='?')

    # Add argument header
    headerHelp = '''To pass the headers value to your HTTP operation, you could
    use -H option. Set the header of the request in the "key:value" format.
    Notice that; you can have multiple headers by having the -H option before
    each header parameter. i. g. httpc -H key1:value2 -H key2:value2 ...'''
    parser.add_argument('-H', '--header', help=headerHelp, action='append')

    # Add arguments data either of -d or -f
    # -d
    dataGroup = parser.add_mutually_exclusive_group()
    dataHelp = '''-d gives the user the possibility to associate the body of
    the HTTP Request with the inline data, meaning a set of characters for
    standard input.'''
    dataGroup.add_argument('-d', '--data', help=dataHelp)

    # -f
    fileHelp = '''  Similarly to -d, -f associate the body of the HTTP Request
    with the data from a given file.'''
    dataGroup.add_argument(
        '-f', '--filename', help=fileHelp, type=str) # keep this aside: type=open

    # Add positional argument URL
    urlHelp = '''URL determines the targeted HTTP server. It could contain
    parameters of the HTTP operation. For example, the URL
    'https://www.google.ca/?q=hello+world' includes the parameter q with
    "hello world" value.'''
    parser.add_argument('URL', help=urlHelp)

    # Add mutually exclusive group: verbose and quiet
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
    '-q', '--quiet', action='store_true', help='only prints header')
    group.add_argument(
    '-v', '--verbose', action='store_true', help='prints header and body')

    parser.add_argument(
    '-o', '--output',
    help='Directs the output to a name of your choice',
    type=argparse.FileType('w'))

    # Argparse Namespace
    args = parser.parse_args()

    # Assign args to variables
    method = args.method
    header = args.header
    data = args.data
    filename = args.filename
    verbose = args.verbose
    quiet = args.quiet
    url = args.URL
    output = args.output

    # Return all variable values
    return method, header, data, filename, verbose, quiet, url, output

# Match return values from getArguments() and assign to their respective variables
method, header, data, filename, verbose, quiet, url, output = getArguments()

def convertListDictToDict(lList):
    return {sItem.split(':')[0]:sItem.split(':')[1] for sItem in lList}

if header:
    header = convertListDictToDict(header)
else:
    header = dict()

# print(method, header, data, filename, verbose, quiet, url, output) # debugging

def urlSanityCheck(sUrl):
    if not re.match('^https?://', sUrl):
        sUrl = 'http://' + sUrl
    return sUrl

def getUrl(sUrl, dHeaders, bVerbose, bQuiet):

    sUrl = urlSanityCheck(sUrl)
    httpHeader = ''
    sHtml = ''
    req = urllib.request.Request(sUrl, headers=dHeaders)
    httpResponse = urllib.request.urlopen(req)
    iHttpCode = httpResponse.getcode()

    if bVerbose or bQuiet:
        httpHeader = httpResponse.info()

    if not bQuiet:
        sHtml = httpResponse.read().decode()

    return httpHeader, sHtml, iHttpCode

def convertStringDictToDict(stringData):

    json_acceptable_string = stringData.replace("'", '"')
    return json.loads(json_acceptable_string)

def readFile(sFilename):

    with open(sFilename) as flFile:
        sFileContent = flFile.read()
    return sFileContent.rstrip()

def postUrl(sUrl, dHeaders, dValues, bVerbose, bQuiet):

    httpHeader = None
    sResponse = None
    strData = urllib.parse.urlencode(dValues)
    byteData = strData.encode()
    req = urllib.request.Request(sUrl, byteData, headers=dHeaders)
    httpResponse = urllib.request.urlopen(req)
    iHttpCode = httpResponse.getcode()

    if bVerbose or bQuiet:
        httpHeader = httpResponse.info()

    if not bQuiet:
        byteResponse = httpResponse.read()
        sResponse = byteResponse.decode()

    return httpHeader, sResponse, iHttpCode

if method == 'get':

    if(data or filename):
        print('-d or -f option only can be used with POST method not GET')
    else:
        header, content, httpCode = getUrl(url, header, verbose, quiet)

if method == 'post':

    if filename:
        sPostData = (convertStringDictToDict(readFile(filename)))
    elif data:
        sPostData = (convertStringDictToDict(data))
    else:
        sPostData = ''

    header, content, httpCode = postUrl(url, header, sPostData, verbose, quiet)

if output:
    if header:
        output.write(str(header))
    if content:
        output.write(str(content))
    print(output.name,'file created!')

if not output:
    if header:
        print(header)
    if content:
        print(content)
        print('Client HTTP Response Code:', httpCode)
