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
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None

    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item
