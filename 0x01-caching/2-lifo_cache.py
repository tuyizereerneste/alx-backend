#!/usr/bin/env python3
""" BaseCache Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Representation of LIFOCache
    """

    def __init__(self):
        """
        Initialize the LIFOCache class with
        the parent's init method
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Method that assign to the dictionary self.cache_data
        the item value for the key
        Arguments:
                key
                item
        Return:
            key - value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.queue[-1]))
                del self.cache_data[self.queue[-1]]
                del self.queue[-1]
            if key in self.queue:
                del self.queue[self.queue.index(key)]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Method that assign to the dictionary self.cache_data
        the item value for the key
        Arguments:
                key
                item
        Return:
            key - value pair
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
