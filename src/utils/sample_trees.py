# -*- coding: utf-8 -*-

from src.structures.bintree import BinTree, leaf

def tree_alpha():
    '''
          A
         / \
        B   C
       / \   \
      D   E   F
    '''
    return BinTree("A",
                   BinTree("B", leaf("D"), leaf("E")),
                   BinTree("C", None, leaf("F")))

def tree_numbers():
    '''
          5
         / \
        2   9
       / \   \
      1   3   12
    '''
    return BinTree(5,
                   BinTree(2, leaf(1), leaf(3)),
                   BinTree(9, None, leaf(12)))

def tree_quest():
    '''
           10
          /  \
         6    15
        / \     \
       2   8     20
          /
         7
    '''
    return BinTree(10,
                   BinTree(6,
                           leaf(2),
                           BinTree(8, leaf(7), None)),
                   BinTree(15, None, leaf(20)))
