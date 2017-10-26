import urllib.request
import urllib.parse

sUrl = 'http://www.youtube.com/watch'
dValues = {'v':'5GzVNi0oTxQ'}
strData = urllib.parse.urlencode(dValues)
byteData = strData.encode()
req = urllib.request.Request(sUrl, byteData)
httpResponse = urllib.request.urlopen(req)
byteResponse = httpResponse.read()
sResponse = byteResponse.decode()
print(sResponse)
