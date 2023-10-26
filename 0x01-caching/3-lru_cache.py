#!/usr/bin/python3
''' LRU Caching module.
'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRU caching algorithm.
    '''

    def __init__(self):
        ''' Initializes the class instance. '''
        super().__init__()
