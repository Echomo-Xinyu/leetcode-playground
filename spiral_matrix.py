# https://leetcode.com/problems/spiral-matrix/

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        visited[j][i] = True
        res.append(matrix[i][j])
        # 0: right, 1: down, 2:left, 3:up
        state = 0
        while True:
            valid = True
            if state == 0:
                if j+1 <= n-1 and visited[i][j+1] == False:
                    j = j + 1
                    visited[i][j] = True
                    res.append(matrix[i][j])
                    continue
                else:
                    state = 1      
            if state == 1:
                if i+1<=m-1 and visited[i+1][j] == False:
                    i = i + 1
                    visited[i][j] = True
                    res.append(matrix[i][j])
                    continue
                else:
                    state = 2
            if state == 2:
                if j-1>=0 and visited[i][j-1] == False:
                    j = j - 1
                    visited[i][j] = True
                    res.append(matrix[i][j])
                    continue
                else:
                    state = 3
            if state == 3:
                if i-1>=0 and visited[i-1][j] == False:
                    i = i - 1
                    visited[i][j] = True
                    res.append(matrix[i][j])
                    continue
                else:
                    state = 0
                    if j+1 <= n-1 and visited[i][j+1] == False:
                        continue
            if valid:
                break
        return res