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
# fl -> file; l -> list
lWordsList = list() # this is the same as lWordsList = list[]
try:
    flHand = open('data\\romeo.txt')
except:
    print('There is no such file.')
else:
    for sLines in flHand:
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
    flHand.close()

    """
    # The random module provides functions that generate pseudorandom numbers
    # (which I will simply call "random" from here on).
    import random
    # To choose an element from a list at random, you can use choice:
    print(random.choice(lWordsList))
    """
