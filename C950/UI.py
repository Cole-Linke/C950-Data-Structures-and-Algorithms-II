# Sources Cited:
# Built-in functions. (n.d.). Python Documentation. https://docs.python.org/3/library/functions.html#sorted
# ANSI Escape sequences. (n.d.). ASCII-Table. https://web.archive.org/web/20201214113226/http://ascii-table.com/ansi-escape-sequences.php
# Sorting techniques. (n.d.). Python Documentation. https://docs.python.org/3/howto/sorting.html
# datetime — Basic date and time types. (n.d.). Python Documentation. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


import datetime


# TIME COMPLEXITY: O(n), n = number of packages
# this method runs a terminal-based interface
# allows the user to return package data for general or time-specific queries
def run_ui(package_hash_table):

    # flag to keep UI looping
    is_running = True

    # TIME COMPLEXITY: O(n log (n)), Timsort sorting algorithm
    while is_running:

        # Print main menu
        print('\n\033[1m--- EOD Package Details ---\033[0m'
              '\n[1] Get all package details'
              '\n[2] Get a specific package\'s details'
              '\n\033[1m--- Time Specific Package Details ---\033[0m'
              '\n[3] Get all package details'
              '\n[4] Get a specific package\'s details'
              '\n--------------------------------------'
              '\n[!] Quit Program')

        try:

            # prompt user for menu selection
            user_input = (input('[ ]: '))

            # [!] Quit Program
            if user_input == '!':
                print('Quitting program')
                is_running = False              # flips flag, ends loop

            # [1] General Details - All Packages
            elif user_input == '1':

                # header section for package table
                print('\nAll Package Details:')
                print('-' * 120)
                print(f"{'ID':<5}| {'Truck':<6}| {'Street':<40}| {'City':<17}| {'Zipcode':<8}| {'Weight':<7}| {'Deadline':<9}| {'Delivered At':<13}")
                print('-' * 120)

                # TIME COMPLEXITY: O(n log (n)), Timsort sorting algorithm
                # iterates through each package in hash table, sorts by ID
                for package in sorted(package_hash_table.get_all_items(), key=lambda p: p.ID):

                    # correct package 9's address at 10:20 AM
                    time_change = datetime.timedelta(hours=10, minutes=20)
                    package.address_update(time_change)

                    # print package information
                    print(f"{package.ID:<5}"                # format output spacing for readability
                          f"| {package.truck_ID:<6}"
                          f"| {package.address:<40}"
                          f"| {package.city:<17}"
                          f"| {package.zipcode:<8}"
                          f"| {package.weight:<7}"
                          f"| {package.deadline:<9}"
                          # format time, output 'N/A' if the package does not have a deliver_time
                          f"| {str(package.delivery_time)[0:8] if package.delivery_time else 'N/A':<13}")
                print('-' * 120)

            # [2] General Details - Specific Package
            elif user_input == '2':
                print('\nWhich package would you like to find:')
                try:
                    # prompt user for package ID
                    target_package = int(input('Package ID: '))
                    # search hash table for the corresponding ID
                    package = package_hash_table.search(target_package)

                    # correct package 9's address at 10:20 AM
                    time_change = datetime.timedelta(hours=10, minutes=20)
                    package.address_update(time_change)

                    # if package was found
                    if package:
                        # header section for target package
                        print(f'\nPackage [{target_package}] details')
                        print('-' * 120)
                        print(f"{'ID':<5}| {'Truck':<6}| {'Street':<40}| {'City':<17}| {'Zipcode':<8}| {'Weight':<7}| {'Deadline':<9}| {'Delivered At':<13}")
                        print('-' * 120)

                        # target package information
                        print(f"{package.ID:<5}"
                              f"| {package.truck_ID:<6}"
                              f"| {package.address:<40}"
                              f"| {package.city:<17}"
                              f"| {package.zipcode:<8}"
                              f"| {package.weight:<7}"
                              f"| {package.deadline:<9}"
                              f"| {str(package.delivery_time)[0:8] if package.delivery_time else 'N/A':<13}")
                        print('-' * 120)
                    else:
                        print(f'No package found with ID {target_package}')      # package ID was not found
                except:
                    print('Invalid Entry. Try again.')

            # [3] Time Specific - All Packages
            elif user_input == '3':
                try:
                    # prompt user for time
                    target_time = input('\nEnter a time [HH:MM:SS]: ')
                    # parse time input
                    h, m, s, = map(int, target_time.strip().split(':'))
                    time_change = datetime.timedelta(hours=h, minutes=m, seconds=s)

                    # update all packages based on time given
                    for package in package_hash_table.get_all_items():
                        # correct package 9's address at 10:20 AM
                        package.address_update(time_change)
                        package.delivery_update(time_change)
                        # delayed packages
                        package.delay_check(time_change)

                    print(f'\nAll Package Details at [{target_time}]')
                    print('-' * 131)
                    print(f"{'ID':<5}| {'Truck':<6}| {'Street':<40}| {'City':<17}| {'Zipcode':<8}| {'Weight':<7}| {'Deadline':<9}| {'Delivered At':<13}| {'Status':<12}")
                    print('-' * 131)

                    for package in sorted(package_hash_table.get_all_items(), key=lambda p: p.ID):
                        print(f"{package.ID:<5}"
                              f"| {package.truck_ID:<6}"
                              f"| {package.address:<40}"
                              f"| {package.city:<17}"
                              f"| {package.zipcode:<8}"
                              f"| {package.weight:<7}"
                              f"| {package.deadline:<9}"
                              # if a package has not been delivered yet, output 'TBD'
                              f"| {str(package.delivery_time)[0:8] 
                                    if package.delivery_time and package.delivery_time <= time_change
                                    else 'TBD'
                                    :<13}"
                              # add status to the output list
                              f"| {package.status:<12}")
                    print('-' * 131)
                except:
                    print("Invalid time format. Use HH:MM:SS")

            # [4] Time Specific - Single Package
            elif user_input == '4':
                print('\nWhich package would you like to find:')

                try:
                    # prompt user for package ID and search the hash table
                    target_package = int(input('Package ID: '))
                    package = package_hash_table.search(target_package)

                    if package:
                        try:
                            # prompt user for time and parse input
                            target_time = input('\nEnter a time [HH:MM:SS]: ')
                            h, m, s, = map(int, target_time.strip().split(':'))
                            time_change = datetime.timedelta(hours=h, minutes=m, seconds=s)

                            # correct package 9's address at 10:20 AM
                            package.address_update(time_change)

                            # update status of target package
                            package.delivery_update(time_change)

                            # delayed packages
                            package.delay_check(time_change)

                            print(f'\nPackage {target_package}\'s details at {target_time}')
                            print('-' * 131)
                            print(f"{'ID':<5}| {'Truck':<6}| {'Street':<40}| {'City':<17}| {'Zipcode':<8}| {'Weight':<7}| {'Deadline':<9}| {'Delivered At':<13}| {'Status':<12}")
                            print('-' * 131)

                            print(f"{package.ID:<5}"
                                  f"| {package.truck_ID:<6}"
                                  f"| {package.address:<40}"
                                  f"| {package.city:<17}"
                                  f"| {package.zipcode:<8}"
                                  f"| {package.weight:<7}"
                                  f"| {package.deadline:<9}"
                                  f"| {str(package.delivery_time)[0:8]
                                  if package.delivery_time and package.delivery_time <= time_change
                                  else 'TBD'
                                  :<13}"
                                  f"| {package.status:<12}")
                            print('-' * 131)
                        except:
                            print("Invalid time format. Use HH:MM:SS")
                    else:
                        print(f'No package found with ID {target_package}')
                except:
                    print('Invalid Entry. Try again.')

            # catch all invalid menu entries
            else:
                print('Invalid entry, Trying again')
        except:
            print('Invalid entry, Trying again')