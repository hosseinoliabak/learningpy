'''
9.2 Write a program that categorizes each mail message by which day of the week
the commit was done. To do this look for lines that start with "From", then
look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
Sample Line:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python assignment9_2_dictionary.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''
