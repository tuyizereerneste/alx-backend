#!/usr/bin/env python3
""" FIFO Module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Representation of FIFO class
    """
    def __init__(self):
        """ Initialisation of class
        """
        super().__init__()
        self.queue = []

    def get(self, key):
        """ Method that return the value in self.cache_data
        linked to key
        Argument:
                key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """ Method that assign to the dictionary self.cache_data
        the item value for the key
        Arguments:
                key
                value
        Return:
                key - value pair
        """
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print("DISCARD: {}".format(self.queue[0]))
            del self.cache_data[self.queue[0]]
            del self.queue[0]
        self.queue.append(key)
        self.cache_data[key] = item
