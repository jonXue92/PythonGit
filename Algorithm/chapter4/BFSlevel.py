# -*- coding: utf-8 -*-

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class BFSLevel:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result