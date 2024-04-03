#!/usr/bin/env python3
""" BasicCache Module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Representation of BasicClass
    """
    def __init__(self):
        """ Initialise BasicCache
        """
        super().__init__()

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
                item
        Return:
            key - value pair
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
