# Source Citation:
# C950 Webinar 2 - Getting Greedy, who moved my data

# class to create hash table using chaining
class ChainingHashTable:

    # TIME COMPLEXITY: O(N), n = initial capacity
    # constructor to initialize the hash table with a capacity of 40
    def __init__(self, initial_capacity=40):
        # initialize table with an empty bucket list
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    # TIME COMPLEXITY: O(N), n = number of items in the bucket
    # insert new item into hash table
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update item if key already exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item  # update value
                return True

        # if it does not exist, append new key-value pair
        key_value = [key, item]
        bucket_list.append(key_value)
        return True


    # TIME COMPLEXITY: 0(N), n = number of items in the bucket
    # searches for an item with matching key in the hash table
    # returns item if found, return None if not found
    def search(self, key):
        # get the bucket list where this key will be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                # if key exists, return its value
                return kv[1]
        # return None if key not found
        return None


    # TIME COMPLEXITY: O(N), n = number of items in the bucket
    # removes an item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where this key will be removed
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0],kv[1]])
                # return true if kv is found and removed
                return True
        # return false if key is not found
        return False


    # TIME COMPLEXITY: O(N), n = total number of key-value pairs
    # print all values stored in hash table (testing purposes)
    def print_table(self):
        for i in range(len(self.table)):
            bucket = self.table[i]
            if bucket:
                print(', '.join(str(kv[1]) for kv in bucket))


    # TIME COMPLEXITY: O(n), n = total number of key-value pairs
    # retrieve all items stored in the hash table
    def get_all_items(self):
        all_items = []
        for bucket in self.table:
            for key, item in bucket:
                all_items.append(item)
        return all_items


    # TIME COMPLEXITY: O(1)
    def __str__(self):
        return f'chaining hash table: {self.table}'
    # TIME COMPLEXITY: O(1)
    def __repr__(self):
        return f'chaining hash table: {self.table}'
