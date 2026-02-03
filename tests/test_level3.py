# -*- coding: utf-8 -*-

import unittest
import random

from src.utils.sample_trees import tree_quest
from src.levels.level3 import shortest_path
from src.structures.queue import Queue
from tests._treegen import random_tree


def collect_nodes(B):
    if B is None:
        return []
    out = []
    stack = [B]
    while len(stack) > 0:
        node = stack.pop()
        out.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return out


def ref_shortest_path(B, start, goal):
    if B is None:
        return []
    if start == goal:
        nodes = collect_nodes(B)
        j = 0
        found = False
        while j < len(nodes) and not found:
            if nodes[j].key == start:
                found = True
            j += 1
        if found:
            return [start]
        return []

    q = Queue()
    parent = {}
    key_to_node = {}

    q.enqueue(B)
    parent[id(B)] = None
    key_to_node[B.key] = B

    while not q.isempty():
        node = q.dequeue()
        if node.left is not None:
            q.enqueue(node.left)
            parent[id(node.left)] = node
            key_to_node[node.left.key] = node.left
        if node.right is not None:
            q.enqueue(node.right)
            parent[id(node.right)] = node
            key_to_node[node.right.key] = node.right

    if (start not in key_to_node) or (goal not in key_to_node):
        return []

    s_node = key_to_node[start]
    g_node = key_to_node[goal]

    s_path = []
    cur = s_node
    while cur is not None:
        s_path.append(cur.key)
        cur = parent[id(cur)]

    g_path = []
    cur = g_node
    while cur is not None:
        g_path.append(cur.key)
        cur = parent[id(cur)]

    s_set = set(s_path)
    lca = None
    k = 0
    while k < len(g_path) and lca is None:
        if g_path[k] in s_set:
            lca = g_path[k]
        k += 1

    # start -> lca
    out = []
    i = 0
    while i < len(s_path) and s_path[i] != lca:
        out.append(s_path[i])
        i += 1
    out.append(lca)

    # lca -> goal (reverse of goal path until lca)
    tail = []
    j = 0
    while j < len(g_path) and g_path[j] != lca:
        tail.append(g_path[j])
        j += 1
    tail.reverse()

    out.extend(tail)
    return out


class TestLevel3(unittest.TestCase):
    def test_fixed_quest(self):
        B = tree_quest()
        self.assertEqual(shortest_path(B, 7, 20), ref_shortest_path(B, 7, 20))
        self.assertEqual(shortest_path(B, 2, 7), ref_shortest_path(B, 2, 7))
        self.assertEqual(shortest_path(B, 6, 20), ref_shortest_path(B, 6, 20))

    def test_missing(self):
        B = tree_quest()
        self.assertEqual(shortest_path(B, 999, 10), [])
        self.assertEqual(shortest_path(B, 10, 999), [])

    def test_random_many(self):
        rng = random.Random(33333)
        t = 0
        while t < 80:
            n = rng.randrange(1, 80)
            B, keys = random_tree(rng, n)

            a = keys[rng.randrange(len(keys))]
            b = keys[rng.randrange(len(keys))]
            got = shortest_path(B, a, b)
            exp = ref_shortest_path(B, a, b)
            self.assertEqual(got, exp)

            # missing cases
            self.assertEqual(shortest_path(B, -1, b), [])
            self.assertEqual(shortest_path(B, a, -1), [])
            t += 1


if __name__ == "__main__":
    unittest.main()
