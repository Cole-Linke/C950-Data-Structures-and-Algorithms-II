# class to create a truck object
class Truck:

    # TIME COMPLEXITY: O(1)
    # initializes a truck object with required attributes
    def __init__(self, ID, speed, package, mileage, address, depart_time):
        self.ID = ID
        self.speed = speed
        self.package = package
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.return_time = None                    # set with return_to_hub function


    # TIME COMPLEXITY: O(1)
    # returns truck's information as a string
    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.speed, self.package, self.mileage,
                                               self.address, self.depart_time)


    # TIME COMPLEXITY: O(1)
    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.speed, self.package, self.mileage,
                                               self.address, self.depart_time)