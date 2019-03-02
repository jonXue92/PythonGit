# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

class NoRecurPreorderTraversal:
    
    def noRecurPreorderTraversal(self, root):
        stack = []
        preorder = []
        if not root:
            return preorder
        
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return preorder