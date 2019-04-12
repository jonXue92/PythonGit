# -*- coding: utf-8 -*-

from collections import deque

class NumIslands:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    islands += 1
        return islands
    
    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = False
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                if not self.is_valid(grid, nx, ny):
                    continue
                queue.append((nx, ny))
                grid[nx][ny] = False
    
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]