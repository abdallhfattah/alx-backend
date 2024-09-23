#!/usr/bin/env python3
"""
  basic caching
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
        # indicate that it been used
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)

        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem()
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)
