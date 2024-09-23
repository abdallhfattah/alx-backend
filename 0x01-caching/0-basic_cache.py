#!/usr/bin/env python3
"""
  basic caching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    """

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
