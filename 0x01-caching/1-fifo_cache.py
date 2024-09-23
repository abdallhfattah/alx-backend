#!/usr/bin/env python3
"""
  basic caching
"""


from queue import Queue
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class utilizing FIFO in strategy to cahce items
    """

    def __init__(self):
        """doc"""
        super().__init__()
        # FIFO mimic
        self.queue = Queue(BaseCaching.MAX_ITEMS)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
