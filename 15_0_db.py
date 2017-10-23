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
conn = sqlite3.connect('employee.db')
c = conn.cursor()
# c.execute("""CREATE TABLE employees(
#              first text,
#              last text,
#              pay real
#           )""")
c.execute("INSERT INTO employees VALUES ('Hossein', 'Oliabak', 80000)")
conn.commit()
conn.close()
