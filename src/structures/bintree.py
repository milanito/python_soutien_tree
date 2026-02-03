# -*- coding: utf-8 -*-

class BinTree:
    '''
    Simple binary tree node:
      - key
      - left
      - right
    '''

    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def leaf(key):
    return BinTree(key, None, None)
