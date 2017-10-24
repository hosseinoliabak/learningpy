'''
JavaScript Object Notation - JSON

JSON (JavaScript Object Notation) is a very popular and lightweight
data-interchange format.It is extensively used when exchanging data among web
services. It is easy for humans to read and write. It is easy for machines to
parse and generate.

Since Python was invented before JavaScript, Python's syntax for dictionaries
and lists influenced the syntax of JSON. So the format of JSON is nearly
identical to a combination of Python lists and dictionaries.

A simple example of JSON notation:
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}

Parsing JSON:
Parsing JSON data with the JSON module using the loads() method.

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# Code: http://www.py4e.com/code3/json2.py
