'''
9.5 First, you have to resolve assignment9_3. This is slightly different.
This program records the domain name (instead of the address) where the message
was sent from instead of who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary.

Sample:
python assignment9_5_dictionary.py
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''
dDomain = dict()
try:
    fiHandle = open("mbox-short.txt")
except:
    print('There is no "mbox-short.txt" file in the same folder as this script.')
else:
    for sLine in fiHandle:
        if not sLine.startswith('From '):
            continue
        lWords = sLine.split()
        lEmailDomain = lWords[1].split('@')
        dDomain[lEmailDomain[1]] = dDomain.get(lEmailDomain[1], 0) + 1
    print (dDomain)
