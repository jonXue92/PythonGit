# -*- coding: utf-8 -*-

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class DFS:
    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)
                
    def connectedSet(self, nodes):
        self.v = {}
        for node in nodes:
            self.v[node.label] = False
        ret = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                ret.append(sorted(tmp))
        return ret
        