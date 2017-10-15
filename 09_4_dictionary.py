'''
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
dWords = dict()
try:
    flHand = open("mbox-short.txt")
except:
    print('There is no "mbox-short.txt" file in the same folder as this script.')
else:
    for sLine in flHand:
        if not sLine.startswith('From '):
            continue
        lWords = sLine.split()
        dWords[lWords[1]] = dWords.get(lWords[1], 0) + 1
    sMax = max(dWords, key = dWords.get)
    print (sMax, dWords[sMax])
