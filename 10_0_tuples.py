'''
Fun fact: The word "tuple" comes from the names given to sequences of numbers of
varying lengths: single, double, triple, quadruple, quituple, sextuple,
septuple, etc.↩


They are much like lists; they have elements which are indexed starting at 0.
But, we are using parentheses "()" and tuples are "immutable". (strings are NOT
immutable also)

Things not to do With Tuples"
    sort
    append
    reverse

Tuples are More Efficient then the lists:
Since Python does not have to build tuple structures to be modifiable, they are
simpler and more efficient in terms of memory use and performance than lists.
So in our program when we are making “temporary variables” we prefer tuples
over lists.

Tuples and Assignment:
(x, y) = (4, 'fred')
Meaning:
x = 4
y = 'fred'

--------------------------------------------------------------------------------
Tuples and Dictionaries:
The items() method in dictionaries returns a list of (key, value) tuples:
>>> d = dict()
>>> d['csev'] = 2
>>> d['cwen'] = 4
>>> for (k,v) in d.items():
...     print(k, v)
...
csev 2
cwen 4

>>> tups = d.items()
>>> print(tups)
dict_items([('csev', 2), ('cwen', 4)])

--------------------------------------------------------------------------------
Tuples are Comparable:
The comparison operators work with tuples and other sequences. If the first
item is equal, Python goes on to the next element, and so on, until it finds
elements that differ. if only one matches, it returns True.

>>> (0, 1, 2) < (5, 1, 2)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
>>> ( 'Jones', 'Sally' ) < ('Jones', 'Sam')
True
>>> ( 'Jones', 'Sally') > ('Adams', 'Sam')
True

--------------------------------------------------------------------------------
Sorting Lists of Tuples:
We can take advantage of the ability to sort a list of tuples to get a sorted
version of a dictionary.
We can do this using the built-in function sorted that takes
a sequence as a parameter and returns a sorted sequence:
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = sorted(d.items())
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> for k, v in sorted(d.items()):
...    print(k, v)
...
a 10
b 1
c 22

Sort by Values Instead of Key:
Taking advantage of "List Comprehensions":
>>> c = {'a':10, 'b':1, 'c':22}

>>> print(sorted([(v, k) for k, v in c.items()]))

[(1, 'b'), (10, 'a'), (22, 'c')]




--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
What do * and ** before a variable name mean in a function signature?

Inside a function header:

* collects all the positional arguments in a tuple

** collects all the keyword arguments in a dictionary

>>> def functionA(*a, **kw):
       print(a)
       print(kw)


>>> functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
(1, 2, 3, 4, 5, 6)
{'a': 2, 'c': 5, 'b': 3}
In a function call:

* unpacks an list or tuple into position arguments

** unpacks an dictionary into keyword arguments

>>> lis=[1, 2, 3, 4]
>>> dic={'a': 10, 'b':20}
>>> functionA(*lis, **dic)  #it is similar to functionA (1, 2, 3, 4, a=10, b=20)
(1, 2, 3, 4)
{'a': 10, 'b': 20}
'''
