# -*- coding: utf-8 -*-

from topSortbfs import DirectedGraphNode

class topSortdfs:
    def topSort(self, graph):
        indegree = {}
        for x in graph:
            indegree[x] = 0
            
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1
                
        ans = []
        for i in graph:
            if indegree[i] == 0:
                self.dfs(i, indegree, ans)
        return ans
    
    def dfs(self, i, indegree, ans):
        # 入度为0的点进入序列,减一代表入度变成-1，防止if countrd[j] == 0这里的判断将点入队
        ans.append(i)
        indegree[i] -= 1
        for j in i.neighbors:
            indegree[j] -= 1
            if indegree[j] == 0:
                self.dfs(j, indegree, ans)