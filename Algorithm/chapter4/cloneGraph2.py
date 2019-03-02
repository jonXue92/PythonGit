# -*- coding: utf-8 -*-

from cloneGraph1 import UndirectGraphNode

# 如果图大的话递归调用会栈溢出
class CloneGraph2:
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        if node is None:
            return None
        
        if node.label in self.dict:
            return self.dict[node.label]
        
        root = UndirectGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))
            
        return root