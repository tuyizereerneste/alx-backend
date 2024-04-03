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
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def put(self, key, item):
        if key or item is None:
            pass
        self.cache_data[key] = item
