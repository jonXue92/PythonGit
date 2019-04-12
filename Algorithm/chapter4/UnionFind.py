# -*- coding: utf-8 -*-

class UnionFind:
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        
        self.father = {i: i for i in range(n)}
        self.size = n
        for u, v in edges:
            self.union(u, v)
        return self.size == 1
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b
            
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
            
        return node