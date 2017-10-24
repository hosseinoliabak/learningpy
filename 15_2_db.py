'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of
email messages per organization (i.e. domain name of the email address) using a
database with the following schema to maintain the counts.
+---------------------------------------------+
|CREATE TABLE Counts (org TEXT, count INTEGER)|
+---------------------------------------------+
If you run the program multiple times in testing or with different files, make
sure to empty out the data before each run.

You can use this code as a starting point for your application:
http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments:
http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results
to the database as each record is read in the loop, it might take as long as a
few minutes to process all the data. The commit insists on completely writing
all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of
the loop. In any database program, there is a balance between the number of
operations you execute between commits and the importance of not losing the
results of operations that have not yet been committed.

Hint: The top organizational count is 536.
'''
import re
import sqlite3

conn = sqlite3.connect('emaildb.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Counts")
c.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
def add_email(sEmail, iCount):
    with conn:
        c.execute("INSERT INTO Counts VALUES (:e, :c)", {'e':sEmail, 'c':iCount})


dOrgStatistics = dict()
sFileName = 'mbox.txt'
flHand = open(sFileName)
sFileContent = flHand.read()
lOrgs = re.findall('From .*@([^ ]*)', sFileContent)
for sOrg in lOrgs:
    dOrgStatistics[sOrg] = dOrgStatistics.get(sOrg, 0) + 1

for keyEmail, valueCount in dOrgStatistics.items():
    add_email(keyEmail, valueCount)

conn.commit()
conn.close()
