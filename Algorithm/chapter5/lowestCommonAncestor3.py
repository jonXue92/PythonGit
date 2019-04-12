# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class LowestCommonAncestor3:
    def lowestCommonAncestor3(self, root, A, B):
        has_A, has_B, LCA = self.helper(root, A, B)
        if has_A and has_B:
            return LCA
        return None
    
    def helper(self, root, A, B):
        if root is None:
            return False, False, None
        left_hA, left_hB, left_LCA = self.helper(root.left, A, B)
        right_hA, right_hB, right_LCA = self.helper(root.right, A, B)
        has_A = root == A or left_hA or right_hA
        has_B = root == B or left_hB or right_hB
        if root == A or root == B:
            return has_A, has_B, root
        if left_LCA and right_LCA:
            return has_A, has_B, root
        if left_LCA:
            return has_A, has_B, left_LCA
        if right_LCA:
            return has_A, has_B, right_LCA
        return has_A, has_B, None