# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

class NoRecurPostorderTraversal:
    
    def noRecurPostorderTraversal(self, root):
        stack = []
        postorder = []
        prev, cur = None, root
        
        if not root:
            return postorder
        
        stack.append(root)
        while len(stack) > 0:
            cur = stack[-1]
            if not prev or prev.left == cur or prev.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left == prev:
                if cur.right:
                    stack.append(cur.right)
            else:
                postorder.append(cur.val)
                stack.pop()
                
        return postorder