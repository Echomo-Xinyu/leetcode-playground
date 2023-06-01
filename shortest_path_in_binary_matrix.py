# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = [[False for _ in range(n)] for _ in range(n)]
        ds = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                ds.append((x, y))
        # ds = {*product(range(-1, 2), range(-1, 2))} - {(0, 0)}
        queue = deque([(0, 0, 1)])
        while queue:
            curr = queue.popleft()
            i, j, step = curr
            if i == n-1 and j == n-1:
                return step
            if visited[i][j]:
                continue

            for di, dj in ds:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        queue.append((ni, nj, step+1))
            visited[i][j] = True
        return -1

    # accepted but not well implemented
    def _1shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        frontier = []
        # i, j, step
        if grid[0][0] == 0:
            frontier.append((0, 0, 1))
        while len(frontier) > 0:
            curr = frontier.pop(0)
            i, j, step = curr
            if visited[i][j] == True:
                continue
            if i == n-1 and j == n-1:
                return step
            if i > 0:
                if j > 0 and grid[i-1][j-1] == 0 and visited[i-1][j-1] == False:
                    frontier.append((i-1, j-1, step+1))
                if grid[i-1][j] == 0 and visited[i-1][j] == False:
                    frontier.append((i-1, j, step+1))
                if j < n-1 and grid[i-1][j+1] == 0 and visited[i-1][j+1] == False:
                    frontier.append((i-1, j+1, step+1))
            if j > 0 and grid[i][j-1] == 0 and visited[i][j-1] == False:
                frontier.append((i, j-1, step+1))
            if j < n-1 and grid[i][j+1] == 0 and visited[i][j+1] == False:
                frontier.append((i, j+1, step+1))
            if i < n-1:
                if j > 0 and grid[i+1][j-1] == 0 and visited[i+1][j-1] == False:
                    frontier.append((i+1, j-1, step+1))
                if grid[i+1][j] == 0 and visited[i+1][j] == False:
                    frontier.append((i+1, j, step+1))
                if j < n-1 and grid[i+1][j+1] == 0 and visited[i+1][j+1] == False:
                    frontier.append((i+1, j+1, step+1))
            visited[i][j] = True
        return -1
