'''
Calling a JSON API

In this assignment, you will write a Python program somewhat similar to
http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON. A place ID is a textual
identifier that uniquely identifies a place as within Google Maps.

API End Points:

To complete this assignment, you should use this API endpoint that has a static
subset of the Google Data:

http://py4e-data.dr-chuck.net/geojson?

This API uses the same parameters (sensor and address) as the Google API.
This API also has no rate limit so you can test as often as you like. If you
visit the URL with no parameters, you get a list of all of the address values
which can be used with this API.
To call the API, you need to provide address that you are requesting as the
address= parameter that is properly URL encoded using the urllib.urlencode()
fuction as shown in http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution:

You can test to see if your program is working with a location of
"South Federal University" which will have a place_id of
"ChIJJ8oO7_B_bIcR2AlhC8nKlok".
+-------------Sample Execution-------------+
|$ python3 solution.py                     |
|Enter location: South Federal University  |
|Retrieving http://...                     |
|Retrieved 2101 characters                 |
|Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok      |
+------------------------------------------+
Turn In:
Please run your program to find the place_id for this location:
+++ University of Malaya +++

Make sure to enter the name and case exactly as above and enter the
place_id and your Python code below. Hint: The first seven characters of the
place_id are "ChIJC9_ ..."
Make sure to retreive the data from the URL specified above and not the normal
Google API. Your program should work with the Google API - but the place_id may
not match for this assignment.
'''
import urllib.request
import json

# Note that Google is increasingly requiring keys for this API
#sServiceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#To use googleapis uncomment the above line and comment the below line
sServiceUrl = 'http://py4e-data.dr-chuck.net/geojson?'

sAddress = input('Enter location [South Federal University]: ')
if not sAddress:
    sAddress = 'South Federal University'

sUrl = sServiceUrl + urllib.parse.urlencode({'address': sAddress})

print('Retrieving', sUrl)
httpResponse = urllib.request.urlopen(sUrl)
sData = httpResponse.read().decode()

try:
    dJsonData = json.loads(sData)
except:
    dJsonData = None

sPlaceID = dJsonData['results'][0]['place_id']
print('place_id:', sPlaceID)
fLat = dJsonData['results'][0]['geometry']['location']['lat']
fLng = dJsonData["results"][0]["geometry"]["location"]["lng"]
print('lat', fLat, 'lng', fLng)
sLocation = dJsonData['results'][0]['formatted_address']
print(sLocation)
