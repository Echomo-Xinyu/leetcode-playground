# https://leetcode.com/problems/word-search/
from typing import List

class Solution:
    # failed attempt
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        frontier = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    frontier.append((i, j))
        for pair in frontier:
            si, sj = pair
            visited = [[False for _ in range(n)] for _ in range(m)]
            f = [(si, sj)]
            k = 0
            new_f = []
            while f:
                while f:
                    i, j = f.pop()
                    if visited[i][j] == False and board[i][j] == word[k]:
                        visited[i][j] = True
                        if i > 0 and visited[i-1][j] != True:
                            new_f.append((i-1, j))
                        if j > 0 and visited[i][j-1] != True:
                            new_f.append((i, j-1))
                        if i + 1 < m and visited[i+1][j] != True:
                            new_f.append((i+1, j))
                        if j + 1 < n and visited[i][j+1] != True:
                            new_f.append((i, j+1))
                if k+1 == len(word):
                    return True
                if new_f:
                    f = new_f
                    new_f = []
                    k += 1
                    if k == len(word):
                        return True
                else:
                    break
        return False
