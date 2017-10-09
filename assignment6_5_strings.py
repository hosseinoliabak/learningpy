'''
Slicing Strings:
[start:end-1]
example: print(sSlice[6:20])
- We can look at any continous section of a string using a colon operator
- The second number is one beyond the end of the slice "up to but not including"
- If the second number is beyond the end of the string, it stops at the end
- [:2] means from character 0 up to 2 (not including character 2)
- [8:] means from character 8 to the end
- [:] means whole the string

find():
We use find() function to search for a substring within another string. find()
finds the first occurrence of the substring. If the substring is not found,
find() returns -1. Remember that string position starts as zero
sFruit = 'banana'
iPosition = sFruit.find('na') #returns 2

also learn about replace(), startswith(), strip(), lstrip(), rstrip() as well as
type() and dir()

6.5 Write code using find() and string slicing (see above) to extract
the number at the end of the line below.

text = "X-DSPAM-Confidence:    0.8475";

Convert the extracted value to a floating point number and print it out.
Desired output: 0.8475
'''
# My variables start with: s -> string; i -> integer; f -> float; b -> boolean
text = "X-DSPAM-Confidence:    0.8475"
iAtPos = text.find('0')
sNumber = text[iAtPos : ]
fNumber = float(sNumber)
print (fNumber)
