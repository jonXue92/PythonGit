# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class LowestCommonAncestor1:
    def lowestCommonAncestor1(self, root, A, B):
        if root is None:
            return None
        if root == A or root == B:
            return root
        left_LCA = self.lowestCommonAncestor1(root.left, A, B)
        right_LCA = self.lowestCommonAncestor1(root.right, A, B)
        # A 和 B 一边一个
        if left_LCA and right_LCA:
            return root
        # 左子树有一个点或者左子树有LCA
        if left_LCA:
            return left_LCA
        # 右子树有一个点或者右子树有LCA
        if right_LCA:
            return right_LCA
        # 左右子树啥都没有
        return None