'''
8.4 Open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to
see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in
alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

Desired Output:
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean
# fi -> file; l -> list
lWordsList = list() # this is the same as lWordsList = list[]
try:
    fiHandle = open("romeo.txt")
except:
    print('There is no "romeo.txt" file in the same folder as this script.')
else:
    for sLines in fiHandle:
        #sLines = sLines.rstrip()
        lLines = sLines.split()
        for sWords in lLines:
            if sWords not in lWordsList:
                lWordsList.append(sWords)
    lWordsList.sort() # Most list methods are void; they modify the list
                      # and return None. If you accidentally write
                      # lWordsList = lWordsList.sort(), you will be
                      # disappointed with the result.
    print(lWordsList)
    fiHandle.close()
