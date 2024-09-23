#!/usr/bin/env python3
"""
  basic caching
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class utilizing FIFO in strategy to cahce items
    """

    def __init__(self):
        """doc"""
        super().__init__()
        # FIFO mimic
        self.cache_data = OrderedDict()

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(True)
            print(f"DISCARD: {first_key}")

