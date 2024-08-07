#!/usr/bin/env python3
""" 0- Basic cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Class BasicCache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
