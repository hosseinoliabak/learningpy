'''
import csv
with open('sample-csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

Another way to read from a csv file is using DictReader() instead of reader()
Read the sample-csv.csv file taking advantage of DictReader()
'''
import csv
with open('sample-csv.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
