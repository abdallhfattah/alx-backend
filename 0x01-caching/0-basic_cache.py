#!/usr/bin/env python3
"""
  basic caching
"""

from typing import override


from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching
    """

    @override
    def get(self, key):
        """Get an item by key

        Args:
            key (any): key to retrive the data

        Returns:
            object : the object associated with the key passed
            None : no key for that item
        """

        if key in self.cache_data:
            return self.cache_data[key]

        return None

    @override
    def put(self, key, object):
        """
        Add an item in the cache


        Args:
            key (any): unquie key for object
            object (any): object
        """
        if (key or object) is None:
            return

        self.cache_data[key] = object
