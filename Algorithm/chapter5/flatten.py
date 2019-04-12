# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Flatten:
    last_node = None
    def flatten(self, root):
        if root is None:
            return
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
        
    def flatten1(self, root):
        self.helper(root)
    
    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return None
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        if right_last is not None:
            return right_last
        if left_last is not None:
            return left_last
        return root