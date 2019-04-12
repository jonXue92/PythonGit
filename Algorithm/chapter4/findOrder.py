# -*- coding: utf-8 -*-

from collections import deque

class FindOrder:
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 0 or prerequisites is None:
            return []
        edges = { x:[] for x in range(numCourses) }
        indegree = [ 0 for x in range(numCourses) ]
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
            edges[prerequisite[1]].append(prerequisite[0])
        queue = deque([ x for x in range(numCourses) if indegree[x] == 0 ])
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for suf in edges[course]:
                indegree[suf] -= 1
                if indegree[suf] == 0:
                    queue.append(suf)
        if len(order) == numCourses:
            return order
        return []