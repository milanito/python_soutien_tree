# -*- coding: utf-8 -*-

import unittest
import random

from src.utils.sample_trees import tree_alpha, tree_numbers, tree_quest
from src.levels.level2 import bfs_lines
from src.structures.queue import Queue
from tests._treegen import random_tree


def ref_bfs_lines(B):
    if B is None:
        return ""
    cur = Queue()
    nxt = Queue()
    cur.enqueue(B)

    lines = []
    while not cur.isempty():
        parts = []
        while not cur.isempty():
            node = cur.dequeue()
            parts.append(str(node.key))
            if node.left is not None:
                nxt.enqueue(node.left)
            if node.right is not None:
                nxt.enqueue(node.right)
        lines.append(" ".join(parts))
        cur, nxt = nxt, cur
    return "\n".join(lines)


class TestLevel2(unittest.TestCase):
    def test_fixed_alpha(self):
        self.assertEqual(bfs_lines(tree_alpha()), ref_bfs_lines(tree_alpha()))

    def test_fixed_numbers(self):
        self.assertEqual(bfs_lines(tree_numbers()), ref_bfs_lines(tree_numbers()))

    def test_fixed_quest(self):
        self.assertEqual(bfs_lines(tree_quest()), ref_bfs_lines(tree_quest()))

    def test_empty(self):
        self.assertEqual(bfs_lines(None), "")

    def test_random_many(self):
        rng = random.Random(22222)
        i = 0
        while i < 120:
            n = rng.randrange(0, 60)
            B, _ = random_tree(rng, n)
            got = bfs_lines(B)
            exp = ref_bfs_lines(B)
            self.assertEqual(got, exp)
            i += 1


if __name__ == "__main__":
    unittest.main()
