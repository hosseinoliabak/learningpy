'''
7.2 Write a program that prompts for a file name, then opens that file and
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
Desired Output: Average spam confidence: 0.750718518519
'''
sFile = input ('Enter the file name [mbox-short.txt]:')
try: # operation_that_can_throw_ioerror()
    flHand = open(sFile)
except: # handle_the_exception_somehow()
    print ('mbox-short.txt is selected.')
    flHand = open('mbox-short.txt')
 #else:
         # we don't want to catch the IOError if it's raised
        #another_operation_that_can_throw_ioerror()
finally: # something_we_always_need_to_do()
    fSum = 0
    iCount = 0
    with flHand:
        for line in flHand:
            if not line.startswith('X-DSPAM-Confidence:') :
                continue
            iAtPos = line.find(':')
            sNumber = line[iAtPos+1 : ]
            fNumber = float(sNumber)
            fSum = fSum + fNumber
            iCount+=1
        print('Average spam confidence:',fSum/iCount)


'''
This will be working on py4e's autograder:
sFile = input ('Enter the file name [mbox-short.txt]:')
flHand = open(sFile)
fSum = 0
iCount = 0
for line in flHand:
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    iAtPos = line.find(':')
    sNumber = line[iAtPos+1 : ]
    fNumber = float(sNumber)
    fSum = fSum + fNumber
    iCount+=1
print('Average spam confidence:',fSum/iCount)
'''
