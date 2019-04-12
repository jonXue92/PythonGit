# -*- coding: utf-8 -*-

class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None

class LowestCommonAncestor2:
    def lowestCommonAncestor2(self, root, A, B):
        dict = {}
        while A is not root:
            dict[A] = True
            A = A.parent
        while B is not root:
            if B in dict:
                return B
            B = B.parent
        return root