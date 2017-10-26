'''
Read the content of sample-csv.csv then produce sample-email.csv wherein
"User Name"s and "Display Name"s are only needed. The delimiter has to be
changed to 'tab' (\t). After running the script The content of sample-email.csv
should be this:

+--------------------------------------+
﻿User Name	Display Name
chris@contoso.com	Chris Green
ben@contoso.com Ben Andrews
david@contoso.com	David Longmuir
cynthia@contoso.com	Cynthia Carey
melissa@contoso.com	Melissa MacBeth
+--------------------------------------+

For this assessment you must use DictReader(), DictWriter(). Other functions
you need to use are: writehedear(), and writerow()
'''
import csv
with open('sample-csv.csv') as csv_file:

    fieldnames = ['User Name', 'Display Name']
    csv_reader = csv.DictReader(csv_file)

    with open('sample-email.csv', 'w') as new_file:

        fieldnames = ['User Name', 'Display Name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        #fieldnames parameter is mandatory for DictWriter

        csv_writer.writeheader()

        for line in csv_reader:
            to_csv = {fieldnames[0]: line['User Name'], fieldnames[1]: line['Display Name']}
            csv_writer.writerow(to_csv)
