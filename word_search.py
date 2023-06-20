# https://leetcode.com/problems/word-search/
from typing import List

class Solution:
    # failed attempt
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # starts
        ss = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    ss.append((i, j))
        for pair in ss:
            si, sj = pair
            f = [(si, sj)]
            # k denote the character to check
            k = 1
            while True:
                next_frontier = []
                while f:
                    i, j = f.pop()
                    if    
        return False

Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
