# class to create a package object
import datetime


class Package:

    # TIME COMPLEXITY: O(1)
    # constructor to initialize a package object with all relevant information
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, notes, status='At Hub', depart_time=None, delivery_time=None, truck_ID=None):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.depart_time = depart_time
        self.delivery_time = delivery_time
        self.truck_ID = truck_ID


    # TIME COMPLEXITY: O(1)
    # returns package information as a string
    def __repr__(self):
        return (
                f"ID: %s \t "
                f"Address: %-20s \t "
                f"City: %s \t "
                f"State: %s \t "
                f"Zip: %s \t "
                f"Deadline: %s \t "
                f"Weight: %s \t "
                f"Notes: %s \t "
                f"Status: %s \t "
                f"Departure Time: %s \t "
                f"Delivery Time: %s \n" %
                (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes, self.status,
                 self.depart_time, self.delivery_time))


    # TIME COMPLEXITY: O(1)
    def __str__(self):
        return (
                f"ID: %s \t "
                f"Address: %-20s \t "
                f"City: %s \t "
                f"State: %s \t "
                f"Zip: %s \t "
                f"Deadline: %s \t "
                f"Weight: %s \t "
                f"Notes: %s \t "
                f"Status: %s \t "
                f"Departure Time: %s \t "
                f"Delivery Time: %s \n" %
                (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes,
                 self.status,
                 self.depart_time, self.delivery_time))


    # TIME COMPLEXITY: O(1)
    # updated the status of package based on a given time
    def delivery_update(self, time_change):
        # not yet left the hub
        if time_change < self.depart_time:
            self.status = 'At Hub'
        # out for delivery
        elif self.depart_time <= time_change < self.delivery_time:
            self.status = 'En Route'
        # has been delivered
        elif time_change >= self.delivery_time:
            self.status = 'Delivered'

    # TIME COMPLEXITY: O(1)
    # corrects the address of package 9 after 10:20 AM
    def address_update(self, time_change):
        # check that package ID is 9 and time is after 10:20 AM
        if self.ID == 9 and time_change >= datetime.timedelta(hours=10, minutes=20):
            self.address = '410 S State St'
            self.city = 'Salt Lake City'
            self.state = 'UT'
            self.zipcode = '84111'

    # TIME COMPLEXITY: O(1)
    # sets status of delayed packaged to delays
    def delay_check(self, time_change):
        # check for certain package IDs and if they have not left yet
        if self.ID in {6, 25, 28, 32}:
            delay_time = datetime.timedelta(hours=9, minutes=5)
            if time_change <= delay_time:
                self.status = 'Delayed until 9:05 AM'
