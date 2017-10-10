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
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line,end='')

# The last code is the same as:
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)


-------------------------------------------------------------------------------
Exercise 1: Write a program to read through a file and print the contents of
the file (line by line) all in upper case. Executing the program will look
as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from
www.py4e.com/code3/mbox-short.txt
'''
# My variables start with: s -> string; i -> integer; f -> float; fi -> file
fiFile = open('mbox-short.txt')
for line in fiFile:
    print(line.upper())
