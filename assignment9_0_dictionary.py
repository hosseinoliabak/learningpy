'''
Comparing Lists and Dictionaries
Dictionaries are like lists except that they use keys instead of numbers to
look up values. Dictionaries are like "associative arrays" in other languages.

----- Lists -----       ----- Dictionaries -----
>>> lst = list()        >>> ddd = dict()
>>> lst.append(21)      >>> ddd['age'] = 21
>>> lst.append(183)     >>> ddd['course'] = 182
>>> print(lst)          >>> print(ddd)
[21, 183]               {'course': 182, 'age': 21}
>>> lst[0] = 23         >>> ddd['age'] = 23
>>> print(lst)          >>> print(ddd)
[23, 183]               {'course': 182, 'age': 23}

* It is an error to reference a key which is not in the dictionary
    >>> ccc = dict()
    >>> print(ccc['csev'])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'csev'

* We can use the in operator to see if a key is in the dictionary
    >>> 'csev' in ccc
    False

The "get" Method for Dictionaries:
The pattern of checking to see if a key is already in a dictionary and assuming
a default value if the key is not there is so common that there is a method
called get() that does this for us

The following 2 codes do the same job;
and produce: {'csev': 2, 'cwen': 2, 'zqian': 1}
1)
dCounts = dict()
lNames = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for sName in lNames :
    if sName not in dCounts:
       dCounts[sName] = 1
    else :
        dCounts[sName] = dCounts[sName] + 1
print(dCounts)

2)
dCounts = dict()
lNames = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for sName in lNames:
    dCounts[sName] = dCounts.get(sName, 0) + 1
print(dCounts)
'''
