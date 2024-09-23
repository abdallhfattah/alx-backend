#!/usr/bin/env python3
'''
  basic caching
'''

from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic Caching
    '''

    def get(self, key):
        '''Get an item by key

        Args:
            key (any): key to retrive the data

        Returns:
            item : the item associated with the key passed
            None : no key for that item
        '''
        self.cache_data.get(key, None)

    def put(self, key, item):
        '''
        Add an item in the cache
        Args:
            key (any): unquie key for item
            item (any): item
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
