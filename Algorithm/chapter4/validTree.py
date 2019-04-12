# -*- coding: utf-8 -*-

from collections import deque

class ValidTree:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        graph = { x: set() for x in range(n) }
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        visited.add(0)
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == n