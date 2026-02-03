# -*- coding: utf-8 -*-

import unittest
from src.structures.bintree import BinTree
from src.levels.level5 import code_list, decode


def prefix_tree():
    '''
             *
            / \
           a   *
              / \
             *   H
            / \
           f   m
    '''
    return BinTree(None,
                   BinTree("a", None, None),
                   BinTree(None,
                           BinTree(None,
                                   BinTree("f", None, None),
                                   BinTree("m", None, None)),
                           BinTree("H", None, None)))


def ref_code_list(T):
    # BFS on (node, code)
    from src.structures.queue import Queue
    q = Queue()
    q.enqueue((T, ""))
    out = []
    while not q.isempty():
        node, code = q.dequeue()
        if node.left is None and node.right is None:
            out.append((node.key, code))
        else:
            q.enqueue((node.left, code + "0"))
            q.enqueue((node.right, code + "1"))
    return out


def ref_decode(T, bits):
    if bits == "":
        return ""
    i = 0
    cur = T
    out = []
    while i < len(bits):
        c = bits[i]
        if c != "0" and c != "1":
            return None
        if c == "0":
            cur = cur.left
        else:
            cur = cur.right
        if cur is None:
            return None
        if cur.left is None and cur.right is None:
            out.append(cur.key)
            cur = T
        i += 1
    if cur is not T:
        return None
    return "".join(out)


class TestLevel5(unittest.TestCase):
    def test_code_list(self):
        T = prefix_tree()
        self.assertEqual(code_list(T), ref_code_list(T))

    def test_decode(self):
        T = prefix_tree()
        self.assertEqual(decode(T, "011100101"), "aHfm")
        self.assertEqual(decode(T, ""), "")
        self.assertEqual(decode(T, "1"), None)
        self.assertEqual(decode(T, "012"), None)
        self.assertEqual(decode(T, "111"), None)


if __name__ == "__main__":
    unittest.main()
