#!/usr/bin/env python3
""" BaseCache Module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Representation of LFUCache class
    """

    def __init__(self):
        """
        Initialize the LFUCache class with
        the parent's init method
        """
        super().__init__()
        self.queue = []
        self.frequency = {}

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
            return
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.queue.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.queue[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.queue[self.queue.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.queue:
                del self.queue[self.queue.index(key)]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Method that return the value in self.cache_data
        linked to key
        Argument:
                key
        """
        if key is not None and key in self.cache_data.keys():
            del self.queue[self.queue.index(key)]
            self.queue.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
