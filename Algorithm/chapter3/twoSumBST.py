# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class TwoSumBST:
    def twoSumBST(self, root, n):
        if not root:
            return None
        self.res = None
        node_set = set()
        self.inorder(root, n, node_set)
        return self.res
    
    def inorder(self, root, n, node_set):
        if not root:
            return
        self.inorder(root.left, n, node_set)
        if n - root.val in node_set:
            self.res = [root.val, n - root.val]
        node_set.add(root.val)
        self.inorder(root.right, n, node_set)
        