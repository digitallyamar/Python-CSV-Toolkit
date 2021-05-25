#########################################################
# This code will create a new csv file containing
# a particular substring present in a row.
#########################################################

import csv

 = 'rent'

fout = open('makaan_rentals.csv', 'w')
writer = csv.writer(fout, delimiter=",")

with open('makaan.csv', 'r') as fin:
    reader = csv.reader(fin, delimiter=",")

    #skip header
    next(reader, None)

    for row in reader:
        if (substring_to_check in row[0]) or 'Rent' in row[0]:
            print('Found Rental property: '  + row[0])
            writer.writerow(row)

fout.close()