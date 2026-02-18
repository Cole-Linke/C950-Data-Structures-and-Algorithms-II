import datetime


# TIME COMPLEXITY: O(n), n = number of addresses in address_reader
# uses target_address to find address ID in address_reader
def load_address(target_address, address_reader):
    for row in address_reader:
        if target_address in row[2]:
            # if the address is found, return the corresponding address ID
            return int(row[0])
    # address not found
    return None


# TIME COMPLEXITY: O(1)
# finds the distance between two addresses
def distance_between(a, b, distance_reader):
    # get distance from a to b in the distance matrix
    distance = distance_reader[a][b]
    # if distance is empty, get distance from b to a
    if distance == '':
        distance = distance_reader[b][a]
    # return distance
    return float(distance)


# TIME COMPLEXITY: O(n), n = number of addresses in address_reader
# calculates distance for the truck to return to the hub and updates truck mileage and return time
def return_to_hub(truck, current_time, distance_reader, address_reader):
    hub_address = '4001 South 700 East'

    # find address ID for truck's current address and the hub address
    return_distance = distance_between(
        load_address(truck.address, address_reader),
        load_address(hub_address, address_reader),
        distance_reader)

    # add return distance to truck's total mileage
    truck.mileage += return_distance
    # update trucks current address to hub address
    truck.address = hub_address
    # calculate and update the truck's return time
    truck.return_time = current_time + datetime.timedelta(hours=return_distance / truck.speed)
    return truck.return_time


# TIME COMPLEXITY: O(n^2), n = number of packages on each truck
# uses nearest neighbor algorithm, delivers packages in order of shortest distance from current location
def delivery(truck, package_hash_table, distance_reader, address_reader):
    # empty list to hold undelivered packages
    undelivered_packages = []

    # loop through each package ID assigned to this truck
    for pack_ID in truck.package:
        # loop up the package in the hash table
        package = package_hash_table.search(pack_ID)
        if package is not None:
            # add package to the undelivered list
            undelivered_packages.append(package)
        else:
            # print warning if package ID was not found
            print(f'Package {pack_ID} not found')

    # clear the truck's package list to reorder during delivery
    truck.package.clear()

    # set current time to the truck's departure time
    current_time = truck.depart_time

    # continue while there are still undelivered packages
    while len(undelivered_packages) > 0:
        # initialize shortest distance to infinity
        shortest_distance = float('inf')
        # placeholder for the next closest package
        next_package = None

        # iterate through all undelivered packages to find the closest one
        for package in undelivered_packages:

            # find the distance between the truck's current address and the package's address
            dist = distance_between(
                    load_address(truck.address, address_reader),
                    load_address(package.address, address_reader),
                    distance_reader)

            # save the shortest package and distance
            if dist < shortest_distance:
                shortest_distance = dist
                next_package = package

        # add the saved package ID to the truck's delivery order
        truck.package.append(next_package.ID)

        # add the distance to the truck's mileage
        truck.mileage += shortest_distance

        # calculate travel time
        travel_time = datetime.timedelta(hours=shortest_distance / truck.speed)
        # add travel time to current time
        current_time += travel_time

        # update truck's current location to the delivered package's location
        truck.address = next_package.address

        # save the departure and delivery time of the package
        next_package.depart_time = truck.depart_time
        next_package.delivery_time = current_time
        next_package.truck_ID = truck.ID

        # remove the delivered package from the undelivered list
        undelivered_packages.remove(next_package)

    # once all packaged are delivered, return truck back to the hub
    return_to_hub(truck, current_time, distance_reader, address_reader)