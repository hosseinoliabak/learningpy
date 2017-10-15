'''
Reading the *Whole* file as a string:

xfile = open('mbox.txt')
inp = xfile.read()
print(len(inp))


File handle as a Sequence
- A file handle open for read can be treated as a sequence of strings where
  each line in the file is a string in the sequence
- We can use the for statement to iterate through a sequence
- Remember - a sequence is an ordered set

xfile = open('mbox.txt')
for line in xfile:
    print(line)


# Searching Through a File:
flHand = open('mbox-short.txt')
for line in flHand:
    if line.startswith('From:') :
        print(line,end='')

# The last code is the same as:
flHand = open('mbox-short.txt')
for line in flHand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)
'''
