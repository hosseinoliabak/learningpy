'''
Musical Track Database
This application will read an iTunes export file in XML and produce a properly
normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files,
make sure to empty out the data before each run.

You can use this code as a starting point for your application:
http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file
to be used for this assignment. You can export your own tracks from iTunes and
create a database, but for the database that you turn in for this assignment,
only use the Library.xml (also available on the current path) that is provided.

To grade this assignment, the program will run a query like this on your
uploaded database and look for the data it expects to see:
+-----------------------------------------------------------------+
|SELECT Track.title, Artist.name, Album.title, Genre.name         |
|    FROM Track JOIN Genre JOIN Album JOIN Artist                 |
|    ON Track.genre_id = Genre.ID and Track.album_id = Album.id   |
|        AND Album.artist_id = Artist.id                          |
|    ORDER BY Artist.name LIMIT 3                                 |
+-----------------------------------------------------------------+

The expected result of the modified query on your database is:
+------------------------------------------------------------------------+
|                 Track                  | Artist |     Album    | Genre |
+----------------------------------------+--------+--------------+-------+
|Chase the Ace                           | AC/DC  | Who Made Who | Rock  |
|D.T.                                    | AC/DC  | Who Made Who | Rock  |
|For Those About To Rock (We Salute You) | AC/DC  | Who Made Who | Rock  |
+----------------------------------------+--------+--------------+-------+

'''
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('music.sqlite')
c = conn.cursor()
c.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre''')

c.execute(""" CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)""")

c.execute(""" CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)""")

c.execute(""" CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)""")

c.execute(""" CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)""")

def lookup(d, sKey):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == sKey:
            found = True
    return None

fHandle = open('Library.xml')
sXml = fHandle.read()
xmlETObj = ET.fromstring(sXml)
lXml = xmlETObj.findall('dict/dict/dict')
for entry in lXml:
        if (lookup(entry, 'Track ID') is None):
            continue
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')
        genre = lookup(entry, 'Genre')

        if name is None or artist is None or album is None or genre is None:
            continue

        c.execute('''INSERT OR IGNORE INTO Artist (name)
            VALUES ( ? )''', ( artist, ))
        c.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = c.fetchone()[0]

        c.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
        c.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = c.fetchone()[0]

        c.execute('''INSERT OR IGNORE INTO Genre (name)
            VALUES ( ? )''', ( genre, ))
        c.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = c.fetchone()[0]

        c.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''', (name, album_id, genre_id, length, rating, count))

conn.commit()
conn.close()
