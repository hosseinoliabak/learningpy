"""
9.1 Write a program that defines the following dictionary:
dStudentMarks = {'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19}
9.1.1 Just print the dictionary (in dictionary form)
{'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19}
9.1.2 Add the key pair value {'Rob':16} to the dictionary
9.1.3 Assign the mark 17 to Joe
9.1.4 Write an If statement that checks for the existence of student 'Mary' in
the dictionary. Print a message that lets you know if 'Mary' is or is not in
the dictionary.
9.1.5 Do the same logic, but this time prompt the user for a student
name. Then apply the same logic as above.
9.1.6 Print the elements of the dictionary, first the key and then the value:
As in:
Joe 15
Mary 20
Ralph 18
Annita 19
"""
dStudentMarks = {'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19}
#------- 9.1.1 -------
print (dStudentMarks)

#------- 9.1.2 -------
dStudentMarks['Joe'] = 17

#------- 9.1.3 -------
dStudentMarks['Rob'] = 16

#------- 9.1.4 -------
bFlag = False
sName = 'Mary'
if sName  in dStudentMarks:
    print(sName,'is in the list :)')
else:
    print('Couldn\'t find',sName,'in the list!')

#------- 9.1.5 -------
bFlag = False
sName = input ('Enter a name: ')
if sName  in dStudentMarks:
    print(sName,'is in the list :)')
else:
    print('Couldn\'t find',sName,'in the list!')
print()
#------- 9.1.6 -------
print('The elements of the dictionary:')
for k,v in dStudentMarks.items():
    print (k,v)
