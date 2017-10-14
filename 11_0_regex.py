'''
The regular expression library re must be imported into your program before you
can use it. The simplest use of the regular expression library is the search()
function. The following program demonstrates a trivial use of the search function.

# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # the caret character is used in
                                  #regular expressions to match "the beginning"
                                  # of a line.
        print(line)

# Code: http://www.py4e.com/code3/re02.py
Now we will only match lines that start with the string "From:". This is a very
simple example that we could have done equivalently with the startswith() method
from the string library.

Without using regular expressions:
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character (.* Matches any character many times)
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy (prefers the shortest))
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy (prefers the shortest))
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

Examples:
-----------------------------------------------------------------
>> y = re.findall('^From (\S+@\S+)',x)
>>> print(y)
['stephen.marquard@uct.ac.za']
-----------------------------------------------------------------
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

['uct.ac.za']
-----------------------------------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Matching and Extracting Data
re.search(): returns a True/False depending on whether the string matches the
regular expression.
re.findall(): if we actually want the matching strings to be extracted.
When we use re.findall(), it returns a list of zero or more sub-strings that
match the regular expression

>>> import re
>>> x = 'My 2 favorite numbers are 19 and 42'
>>> y = re.findall('[0-9]+',x)
>>> print(y)
['2', '19', '42']

>>> y = re.findall('[AEIOU]+',x)
>>> print(y)
[]

'''
