#!/usr/bin/env python3
""" 3- LFU cache """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Class LFUCache
    """
    def __init__(self):
        """ Initializing
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                else:
                    lfu_key = min(self.frequency, key=self.frequency.get)
                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.frequency[key] = self.frequency.get(key, 0) + 1
            return self.cache_data.get(key)
        return None
