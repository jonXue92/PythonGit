# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

class NoRecurInorderTraversal:
    
    def noRecurInorderTraversal(self, root):
        stack = []
        inorder = []
        while root:
            stack.append(root)
            root = root.left
            
        while len(stack) > 0:
            node = stack[-1]
            inorder.append(node.val)
            
            if not node.right:
                node = stack.pop()
                while len(stack) > 0 and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return inorder