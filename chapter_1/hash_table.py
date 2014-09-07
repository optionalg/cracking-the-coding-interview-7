

class hash_table(object):

    def __init__(self):
        self.table = []

    def _hash_function(self, item):
        """
        maps an item and the slot in the table
        where the item belongs. takes any item in collection
        and returns an integer in the range of slot names,
        between 0 and m-1.

        this hash function takes an item and divides it by
        the table size, returning the remainder as its hash value
        """
        hash_value = item % len(self.table)
