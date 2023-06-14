# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if not n:
            return 0
        m = len(grid[0])
        if not m:
            return 0

        grid_copy = [[grid[i][j] for j in range(m)] for i in range(n)]
        dxdy = ((-1, 0), (1, 0), (0, 1), (0, -1))
                
        def dfs(x, y):
            grid_copy[x][y] = '0'
            for dx, dy in dxdy:
                x_new, y_new = x + dx, y + dy
                if not (0 <= x_new < n and 0 <= y_new < m):
                    continue
                if grid_copy[x_new][y_new] == '0':
                    continue
                dfs(x_new, y_new)
            return
        
        cnt = 0
        for x in range(n):
            for y in range(m):
                if grid_copy[x][y] == '1':
                    cnt += 1
                    dfs(x, y)
        return cnt

    # accepted but can be more concise
    def _1numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        num = 0
        frontier = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    num += 1
                    visited[i][j] = True
                    frontier.append((i, j))
                    while frontier:
                        curr = frontier.pop()
                        l, m = curr
                        visited[l][m] = True
                        if l > 0 and grid[l-1][m] == "1" and not visited[l-1][m]:
                            frontier.append((l-1, m))
                        if l + 1 < len(grid) and grid[l+1][m] == "1" and not visited[l+1][m]:
                            frontier.append((l+1, m))
                        if m > 0 and grid[l][m-1] == "1" and not visited[l][m-1]:
                            frontier.append((l, m-1))
                        if m + 1 < len(grid[0]) and grid[l][m+1] == "1" and not visited[l][m+1]:
                            frontier.append((l, m+1))
        return num
