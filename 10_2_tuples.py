'''
10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
econd time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.

Desired Output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
dHours = dict()
try:
    flHand = open("mbox-short.txt")
except:
    print('There is no "mbox-short.txt" file in the same folder as this script.')
else:
    for sLine in flHand:
        if not sLine.startswith('From '):
            continue
        lWords = sLine.split()
        lHours = lWords[5].split(':')
        dHours[lHours[0]] = dHours.get(lHours[0], 0) + 1
    for k, v in sorted(dHours.items()):
        print (k, v)
