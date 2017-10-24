'''
Instructions
If you don't already have it, install the SQLite Browser from
http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table
in the database called "Ages":

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously
inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Oz', 25);
INSERT INTO Ages (name, age) VALUES ('Noor', 31);
INSERT INTO Ages (name, age) VALUES ('Praise', 22);
INSERT INTO Ages (name, age) VALUES ('Kerris', 26);
INSERT INTO Ages (name, age) VALUES ('Louise', 19);
INSERT INTO Ages (name, age) VALUES ('Ismaeel', 17);

Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

Find the first row in the resulting record set and enter the long string that
looks like 53656C696E613333.

Note: This assignment must be done using SQLite - in particular, the SELECT
query above will not work in any other database. So you cannot use MySQL or
Oracle for this assignment.
'''
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})

# dPeople = {'Oz': 25, 'Noor': 31, 'Praise': 22, 'Kerris': 26, 'Louise': 19, 'Ismaeel': 17 }
# for keyName, valueAge in dPeople.items():
#     add_people(keyName, valueAge)

# Or what I prefer
lPeople = [('Oz', 25), ('Noor', 31), ('Praise', 22), ('Kerris', 26), ('Louise', 19), ('Ismaeel', 17)]
for tItem in lPeople:
    sName, iAge = tItem
    add_people(sName, iAge)

c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(c.fetchall())

conn.commit()
conn.close()
