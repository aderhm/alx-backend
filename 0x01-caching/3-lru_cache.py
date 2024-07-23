#!/usr/bin/env python3
""" 3- LRU cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Class LRUCache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                else:
                    li_key = next(iter(self.cache_data))
                    print(f"DISCARD: {li_key}")
                    del self.cache_data[li_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
            return self.cache_data.get(key)
        return None
