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
- [::-1] this is a handy way of reversing a string

find():
We use find() function to search for a substring within another string. find()
finds the first occurrence of the substring. If the substring is not found,
find() returns -1. Remember that string position starts as zero
sFruit = 'banana'
iPosition = sFruit.find('na') #returns 2

also learn about replace(), startswith(), strip(), lstrip(), rstrip() as well as
type() and dir()
'''
