#!/usr/bin/env python3
"""
  basic caching
"""

from typing import override

from queue import Queue

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class utilizing FIFO in strategy to cahce items
    """

    def __init__(self):
        """doc"""
        super.__init__()
        # FIFO mimic
        self.queue = Queue(maxlen=super.MAX_ITEMS)

    @override
    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

    @override
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if self.queue.full():
            key = self.queue.get()
            self.cache_data.pop(key)
            print("DISCARD: {}".format(key))

        self.queue.put(key)
        self.cache_data[key] = item
