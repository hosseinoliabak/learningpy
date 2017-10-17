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



Main file processing modes:

'r' Open for reading (Default). The file pointer is placed at the beginning of
    the file.

'w' Open for writing. Overwrites the file if the file exists. If the file does
    not exist, creates a new file for writing.

'a' Open for appending to the end of the file. The file pointer is at the end
    of the file if the file exists. That is, the file is in the append mode. If
    the file does not exist, it creates a new file for writing.

'b' Binary Mode

'+' ('r+', 'w+') Open a file for reading and writing
'''
