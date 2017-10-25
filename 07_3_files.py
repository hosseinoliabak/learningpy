'''
Writing to a text file:
f = open('legend.txt', 'w')
f.write('Harry Potter was a highly unusual boy in many ways.\n')
f.write('His siter, Mary, had a little lamb\n')
This set of instructions will write couple of string to a file called legend.txt.
It is important to notice that if the file ‘legend.txt’ already exists, then it
will be deleted when we call open.

Apending to a text file (the file will no be deleted, and the data will be
appended to it):
f = open('legend.txt', 'a')
f.write('This is the continuation of the story.\n')

We can check for the existence of a file this way:
import os
if os.path.isfile('legend.txt'):
    print('legend.txt already exists')

Binary Files:
When you open a file in binary mode, you read and write a sequence of bytes.
That is, you have access to the individual bytes in the file.

Opening a picture file in binary mode:
f = open('pic.jpg', 'rb')
#Reading 6 bytes from the file:
somedata = f.read(6)
print('somedata: ', somedata)

somedata: b'\xff\xd8\xff\xe0\x00\x10'

---------------------------------Other Methods----------------------------------
You can use the remove() method to delete files by supplying the name of the
file to be deleted as the argument:
os.remove(file_name)

The rmdir() method deletes the directory, which is passed as an argument in
the method. Before removing a directory, all the contents in it should be
removed:
os.rmdir('dirname')

The listdir(path) returns a list containing the names of the entries in the
directory given by path:
os.listdir(path)

The rename() method takes two arguments, the current filename and the new filename:
os.rename(current_file_name, new_file_name)

+-----------------------Bulk Rename Example--------------------+
|import os                                                     |
|                                                              |
|def rename(directory):                                        |
|    for sName in os.listdir(directory):                       |
|        if sName.startswith('2016'):                          |
|            os.rename(sName, (sName[:3] + '7' + sName[4:]))   |
|rename('c:\py')                                               |
+--------------------------------------------------------------+

Using the "with" statement to open files:
with open("welcome.txt", "r") as myfile:
    data = myfile.read()
    do something with data

Notice, that we didn't have to write "file.close()". That will automatically be
called. That is one of the advantages of using the with statement to open files.
The with statement is an example of working with context managers.
'''
