# -*- coding: utf-8 -*-

import random
from src.structures.bintree import BinTree

def random_tree(rng, n):
    '''
    Build a random binary tree with n nodes.
    Keys are unique ints.
    Returns (root, keys_list).
    '''
    if n <= 0:
        return (None, [])

    keys = list(range(n))
    rng.shuffle(keys)

    root = BinTree(keys[0], None, None)
    nodes = [root]
    i = 1

    while i < n:
        parent = nodes[rng.randrange(len(nodes))]
        new_node = BinTree(keys[i], None, None)
        i += 1

        # try to attach left or right; if full, pick another parent
        tries = 0
        attached = False
        while tries < 10 and not attached:
            side = rng.randrange(2)
            if side == 0:
                if parent.left is None:
                    parent.left = new_node
                    attached = True
                else:
                    parent = nodes[rng.randrange(len(nodes))]
            else:
                if parent.right is None:
                    parent.right = new_node
                    attached = True
                else:
                    parent = nodes[rng.randrange(len(nodes))]
            tries += 1

        if not attached:
            # fallback: find first parent with free slot
            j = 0
            while j < len(nodes) and not attached:
                if nodes[j].left is None:
                    nodes[j].left = new_node
                    attached = True
                elif nodes[j].right is None:
                    nodes[j].right = new_node
                    attached = True
                j += 1

        nodes.append(new_node)

    return (root, keys)
