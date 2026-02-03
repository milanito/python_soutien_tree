# -*- coding: utf-8 -*-

import unittest
import random

from src.utils.sample_trees import tree_alpha, tree_numbers, tree_quest
from src.levels.level1 import serialize_preorder
from tests._treegen import random_tree


def ref_serialize_preorder(B):
    if B is None:
        return "."
    return str(B.key) + "(" + ref_serialize_preorder(B.left) + ")(" + ref_serialize_preorder(B.right) + ")"


class TestLevel1(unittest.TestCase):
    def test_fixed_alpha(self):
        self.assertEqual(serialize_preorder(tree_alpha()), ref_serialize_preorder(tree_alpha()))

    def test_fixed_numbers(self):
        self.assertEqual(serialize_preorder(tree_numbers()), ref_serialize_preorder(tree_numbers()))

    def test_fixed_quest(self):
        self.assertEqual(serialize_preorder(tree_quest()), ref_serialize_preorder(tree_quest()))

    def test_empty(self):
        self.assertEqual(serialize_preorder(None), ".")

    def test_random_many(self):
        rng = random.Random(12345)
        k = 0
        while k < 120:
            n = rng.randrange(0, 35)
            B, _ = random_tree(rng, n)
            got = serialize_preorder(B)
            exp = ref_serialize_preorder(B)
            self.assertEqual(got, exp)
            k += 1


if __name__ == "__main__":
    unittest.main()
