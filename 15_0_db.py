'''
Terminology
- Database - contains many tables
    - Relation (or table) - contains tuples and attributes
        - Tuple (or row) - a set of fields that generally represents an
        “object” like a person or a music track
        - Attribute (also column or field) - one of possibly many elements of
        data corresponding to the object represented by the row

Database Model
A database model or database schema is the structure or format of a database,
described in a formal language supported by the database management system.
In other words, a “database model” is the application of a data model when used
in conjunction with a database management system.
'''
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees(
             first text,
             last text,
             pay real
          )""")
# The followings are prone to SQL injection:
c.execute("INSERT INTO employees VALUES ('Hossein', 'Oliabak', 80000)")
c.execute("INSERT INTO employees VALUES ('Iman', 'Gh', 90000)")
c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format('Ryan', 'Oliabak', '100000'))

# The correct way:
c.execute("INSERT INTO employees VALUES (?, ?, ?)",("John", "Doe", "80000"))
#OR
c.execute("INSERT INTO employees VALUES (:f, :l, :p)",{'f':'Jane', 'l':'Doe', 'p':90000})


#The incorrect way to read data
c.execute("SELECT * FROM employees WHERE last = 'Oliabak'")
print(c.fetchall())

#The correct way to read data
c.execute("SELECT * FROM employees WHERE last = ?", ('Doe',))
print(c.fetchall())

#OR
c.execute("SELECT * FROM employees WHERE last = :last", {'last':'Gh'})
print(c.fetchall())

conn.commit()
conn.close()
