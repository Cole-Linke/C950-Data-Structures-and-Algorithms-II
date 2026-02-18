# Source Citation:
# CSV — CSV file reading and writing. (n.d.). Python Documentation. https://docs.python.org/3/library/csv.html#csv.reader

import csv
from ChainingHashTable import ChainingHashTable
from Package import Package


# TIME COMPLEXITY: O(n), n = number of lines in CSV file
# loads the distance and address data from distance.csv and address.csv
def load_csv_files():
    with open('CSV/Distance_Table.csv') as csvfile:
        # reads Distance_Table.csv and puts it into a list of rows
        distance_reader = list(csv.reader(csvfile))

    with open('CSV/Address_Table.csv') as csvfile1:
        # reads Address_Table.csv and puts it into a list of rows
        address_reader = list(csv.reader(csvfile1))

    # return both csv tables
    return distance_reader, address_reader


# TIME COMPLEXITY: O(N), n = number of packages in CSV file
# loads package data from csv and stores it in a hash table
def load_packages(filename):
    # initialize chaining hash table
    package_hash_table = ChainingHashTable()

    # Open the CSV file
    with open(filename, encoding='utf-8-sig') as packages:
        # Create an object to read CSV file
        package_reader = csv.reader(packages, delimiter=',')

        # process each row in csv file
        for package in package_reader:
            if len(package) < 7:
                continue        # skips rows with missing required fields

            # Extract package fields from the row
            pack_ID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            # change kilos to kg for formatting reasons
            weight = package[6].replace(' Kilos', 'kg')
            notes = package[7] if len(package) > 7 else ''

            # create package object and insert into hash table
            package_hash_table.insert(pack_ID, Package(pack_ID, address, city, state, zipcode, deadline, weight, notes))

    return package_hash_table