'''
import csv
with open('sample-csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

Another way to read from a csv file is using DictReader() instead of reader()
Read the sample-csv.csv file taking advantage of DictReader()
'''
# The variables start with:
# s -> string; i -> integer; f -> float; b -> boolean; fl -> file;
# t -> tuples; l -> list; d -> dictionary; od -> ordered dictionary;
# byte -> bytes; sock -> socket object; bs -> BeautifulSoup object
import csv
with open('sample-csv.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for odLine in csv_reader:
        print(odLine)
