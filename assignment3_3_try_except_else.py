'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is
out of range, print an error. If the score is between 0.0 and 1.0, print a
grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and
exit. For the test, enter a score of 0.85.
'''
sScore = input('Enter the score between 0.0 and 1.0: ')
try:
    fScore = float(sScore)
except:
    sGrade = "Please enter a valid data format"
else:
    if fScore < 0 or fScore > 1:
        sGrade = "The value must be between 0.0 and 1.0"
    elif fScore >= 0.9:
        sGrade = "A"
    elif fScore >= 0.8:
        sGrade = "B"
    elif fScore >= 0.7:
        sGrade = "C"
    elif fScore >= 0.6:
        sGrade = "D"
    elif fScore < 0.6:
        sGrade = "F"

print (sGrade)
