'''
continue vs break
 - break skips out of the loop.
 - continue skips to the top of the loop.

5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the
number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''
iLargest = None
iSmallest =None
while True:
    sInput = input('Enter and Integer or stop entering by typing "done": ')
    if str.lower(sInput) == 'done' : break
    try:
        iInput = int(sInput)
    except:
        print('Invalid input')
    else:
        if iLargest is None or iInput > iLargest:
            iLargest = iInput
        if iSmallest is None or iInput < iSmallest:
            iSmallest = iInput

print ("Maximum is", iLargest)
print ("Minimum is", iSmallest)
