# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
