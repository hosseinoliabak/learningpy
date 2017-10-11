'''
Comparing Lists and Dictionaries
Dictionaries are like lists except that they use keys instead of numbers to
look up values

----- Lists -----       ----- Dictionaries -----
>>> lst = list()        >>> ddd = dict()
>>> lst.append(21)      >>> ddd['age'] = 21
>>> lst.append(183)     >>> ddd['course'] = 182
>>> print(lst)          >>> print(ddd)
[21, 183]               {'course': 182, 'age': 21}
>>> lst[0] = 23         >>> ddd['age'] = 23
>>> print(lst)          >>> print(ddd)
[23, 183]               {'course': 182, 'age': 23}


9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.

Desired Output:
cwen@iupui.edu 5
'''
