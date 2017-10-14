'''
Write a program to read through a mail log, build a histogram using a
dictionary to count how many messages have come from each email address, and
print the dictionary.

Desired Output
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean
# fi -> file; l -> list; d -> dictionary
dWords = dict()
try:
    fiHandle = open("mbox-short.txt")
except:
    print('There is no "mbox-short.txt" file in the same folder as this script.')
else:
    for sLine in fiHandle:
        if not sLine.startswith('From '):
            continue
        lWords = sLine.split()
        dWords[lWords[1]] = dWords.get(lWords[1], 0) + 1
    print(dWords)
