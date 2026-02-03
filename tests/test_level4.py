# -*- coding: utf-8 -*-

import unittest
import random

from src.utils.sample_trees import tree_quest
from src.levels.level4 import kinship
from tests._treegen import random_tree


def find_node(B, target):
    if B is None:
        return None
    if B.key == target:
        return B
    left = find_node(B.left, target)
    if left is not None:
        return left
    return find_node(B.right, target)


def ref_distance_down(B, target, dist):
    if B is None:
        return -1
    if B.key == target:
        return dist
    d = ref_distance_down(B.left, target, dist + 1)
    if d != -1:
        return d
    return ref_distance_down(B.right, target, dist + 1)


def ref_kinship(B, x, y):
    if B is None:
        return -1
    if x == y:
        node = find_node(B, x)
        if node is None:
            return -1
        return 0

    nx = find_node(B, x)
    ny = find_node(B, y)
    if nx is None or ny is None:
        return -1

    d = ref_distance_down(nx, y, 0)
    if d != -1:
        return d
    d = ref_distance_down(ny, x, 0)
    if d != -1:
        return d
    return -1


class TestLevel4(unittest.TestCase):
    def test_fixed(self):
        B = tree_quest()
        self.assertEqual(kinship(B, 10, 10), 0)
        self.assertEqual(kinship(B, 10, 7), 3)
        self.assertEqual(kinship(B, 6, 7), 2)
        self.assertEqual(kinship(B, 8, 2), -1)
        self.assertEqual(kinship(B, 20, 10), 2)

    def test_random_many(self):
        rng = random.Random(44444)
        i = 0
        while i < 120:
            n = rng.randrange(1, 80)
            B, keys = random_tree(rng, n)
            a = keys[rng.randrange(len(keys))]
            b = keys[rng.randrange(len(keys))]
            got = kinship(B, a, b)
            exp = ref_kinship(B, a, b)
            self.assertEqual(got, exp)
            self.assertEqual(kinship(B, -1, b), -1)
            self.assertEqual(kinship(B, a, -1), -1)
            i += 1


if __name__ == "__main__":
    unittest.main()
