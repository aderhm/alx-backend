#!/usr/bin/env python3
""" 0- Fifo cache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFOCache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                fi_key = next(iter(self.cache_data))
                print(f"DISCARD: {fi_key}")
                del self.cache_data[fi_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
