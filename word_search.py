# https://leetcode.com/problems/word-search/
from typing import List
#TODO

class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(borad[0])):
                if dfs(board, i, j, word):
                    return True
        return False
    
    def dfs(board, i, j, word):
        if len(word) == 0:
            retur True
        if i < 0 or i >= len(board) or j < 0 or j > len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        w = word[1:]
        res = dfs(board, i+1, j, w) or dfs(board, i-1, j, w) or dfs(board, i, j-1, w) or dfs(board, i, j+1, w)
        board[i][j] = temp
        return res



    # failed attempt
    def _1exist(self, board: List[List[str]], word: str) -> bool:
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
