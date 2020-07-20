'''
Full description:
https://www.hackerrank.com/challenges/swap-nodes-algo/problem

contains three sub-problems:
- build tree from a specific input (see 'def build_tree')
- swap nodes (see 'def swapNodes')
- print inorder traversal (see 'def traverse')

'''

import os
import sys

sys.setrecursionlimit(1500) #some test cases don't pass due to recursion limit

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(indexes):
    root = Node(1)
    queue = [root]
    for left, right in indexes:
        cur = queue.pop(0)
        if left >= 0:
            left_node = Node(left)
            cur.left = left_node
            queue.append(left_node)
        if right >= 0:
            right_node = Node(right)
            cur.right = right_node
            queue.append(right_node)
    return root

def traverse(node, s=[]):
    if not node:
        return
    traverse(node.left, s)
    s.append(str(node.val))
    traverse(node.right, s)
    return s

def swapNodes(indexes, queries):
    root = build_tree(indexes)
    result = []
    for query in queries:
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if level % query == 0:
                node.left, node.right = node.right, node.left
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        result.append(traverse(root, []))
    return result

