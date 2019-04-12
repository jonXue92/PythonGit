# -*- coding: utf-8 -*-

class SequenceReconstruction:
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org
    
    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
        return graph
    
    def get_indegrees(self, graph):
        indegrees = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
    
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        queue = [node for node in graph if indegrees[node] == 0]
        topo_order = []
        while queue:
            if len(queue) > 1:
                return None
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
        return None