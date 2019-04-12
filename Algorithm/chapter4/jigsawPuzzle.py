# -*- coding: utf-8 -*-

from collections import deque

class JigsawPuzzle:
    def hash(self, tmp):
        t = 0
        for i in tmp:
            t = t * 10 + i
        return t
    def bfs(self, mat, ans):
        if mat == ans:
            return "YES"
        hashans = self.hash(ans)
        visit = set()
        move = [[0,1],[0,-1],[1,0],[-1,0]]
        g = [[] for i in range(9)]
        for i in range(3):
            for j in range(3):
                for k in range(4):
                    ti = i + move[k][0]
                    tj = j + move[k][1]
                    if ti >= 0 and ti < 3 and tj >= 0 and tj < 3:
                        g[i * 3 + j].append(ti * 3 + tj)
        q = deque(self.hash(mat))
        visit.add(self.hash(mat))
        while q:
            Front = q.popleft()
            tmp = []
            while Front:
                tmp.append(Front % 10)
                Front = Front // 10
            if len(tmp) == 8:
                tmp.append(0)
            tmp = tmp[::-1]
            
            for pos in range(9):
                if tmp[pos] == 0:
                    break
            for i in g[pos]:
                tmp[pos], tmp[i] = tmp[i], tmp[pos]
                hashvalue = self.hash(tmp)
                if hashvalue == hashans:
                    return "YES"
                if hashvalue not in visit:
                    visit.add(hashvalue)
                    q.append(hashvalue)
                tmp[pos], tmp[i] = tmp[i], tmp[pos]
                
        return "NO"
    
    def jigsawPuzzle(self, matrix):
        ansmat = [[1,2,3],[4,5,6],[7,8,0]]
        ans, mat = [], []
        for i in ansmat:
            for j in i:
                ans.append(j)
        for i in matrix:
            for j in i:
                mat.append(j)
        return self.bfs(mat, ans)