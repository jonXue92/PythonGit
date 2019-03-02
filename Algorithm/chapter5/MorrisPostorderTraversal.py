# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

class MorrisPostorderTraversal:
    def morrisPostorderTraversal(self, root):
        nums = []
        cur = None
        
        while root:
            if root.right != None:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left
                if cur.left == root:
                    cur.left = None
                    root = root.left
                else:
                    nums.append(root.val)
                    cur.left = root
                    root = root.right
            else:
                nums.append(root.val)
                root = root.left
                
        nums.reverse()
        return nums