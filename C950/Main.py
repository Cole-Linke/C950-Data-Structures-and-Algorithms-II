# Cole Linke
# Student ID: 011917160
# C950 WGUPS Routing Program Implementation

import datetime

# import modules
from CSV_Import import load_csv_files, load_packages
from Delivery import delivery, return_to_hub, distance_between, load_address
from Truck import Truck
from UI import run_ui


# TIME COMPLEXITY: O(1)
# create truck objects

# create and assign truck1 with packages, leaves at 8:00:01 AM
truck1 = Truck(1, 18,  [1, 4, 5, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40],
                     0.0, '4001 South 700 East', datetime.timedelta(hours=8, minutes=0, seconds=1))

# create and assign truck2 with packages, leaves at 9:05:01 AM
truck2 = Truck(2, 18, [3, 6, 8, 18, 25, 26, 28, 32, 36, 38],
                     0.0, '4001 South 700 East', datetime.timedelta(hours=9, minutes=5, seconds=1))

# create and assign truck3 with packages, leaves at 10:20:01 AM
truck3 = Truck(3, 18, [2, 7, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39],
                     0.0, '4001 South 700 East', datetime.timedelta(hours=10, minutes=20, seconds=1))


# TIME COMPLEXITY: O(n), n = number of lines in CSV file
# load CSV data

# load distance and address data
distance_reader, address_reader = load_csv_files()
# load package data into hash table
package_hash_table = load_packages('CSV/Package_Table.csv')


# TIME COMPLEXITY: O(n^2), n = number of packages on the truck
# deliver packages

# run delivery algo for both truck1 and truck2
delivery(truck1, package_hash_table, distance_reader, address_reader)
delivery(truck2, package_hash_table, distance_reader, address_reader)
# make truck3 wait until its either 10:20:01 AM or another truck has returned to the hub
truck3.depart_time = max(datetime.timedelta(hours=10, minutes=20, seconds=1), min(truck1.return_time, truck2.return_time))
# run delivery algo for truck3
delivery(truck3, package_hash_table, distance_reader, address_reader)


# print author header
print('\nCole Linke'
      '\nID: 011917160')

# print formatted summary for each truck
print('\n\033[1m--- Truck One Details ---\033[0m')
print(f'Depart Time:   {truck1.depart_time}')           # time truck left the hub
print(f'Return Time:   {truck1.return_time}')           # time truck returned to the hub
print(f'Total Mileage: {round(truck1.mileage, 1)}')     # mileage for select truck
print('\033[1m--- Truck Two Details ---\033[0m')
print(f'Depart Time:   {truck2.depart_time}')
print(f'Return Time:   {truck2.return_time}')
print(f'Total Mileage: {round(truck2.mileage, 1)}')
print('\033[1m--- Truck Three Details ---\033[0m')
print(f'Depart Time:   {truck3.depart_time}')
print(f'Return Time:   {truck3.return_time}')
print(f'Total Mileage: {round(truck3.mileage, 1)}')
print('-' * 27)
total_mileage = round(truck1.mileage + truck2.mileage + truck3.mileage, 1)
print(f'Total Truck Mileage: {total_mileage}')          # total mileage for all 3 trucks


# TIME COMPLEXITY: O(n)
# run user interface
run_ui(package_hash_table)

