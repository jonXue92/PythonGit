# -*- coding: utf-8 -*-

from BFSlevel import TreeNode
from collections import deque

class Serialize:
    def serialize(self, root):
        if not root:
            return "{}"
        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(bfs_order)
    
    def deserialize(self, data):
        if not data:
            return None
        bfs_order = [TreeNode(int(val)) if val != '#' else None 
                     for val in data.split()]
        root = bfs_order[0]
        fast_index = 1
        
        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root