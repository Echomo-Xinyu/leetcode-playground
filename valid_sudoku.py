# https://leetcode.com/problems/valid-sudoku/
from typing import List

# only existed values need to be validated
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            curr_row = set()
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    continue
                else:
                    if ch in curr_row:
                        return False
                    curr_row.add(ch)
        for i in range(9):
            curr_col = set()
            for j in range(9):
                ch = board[j][i]
                if ch == ".":
                    continue
                else:
                    if ch in curr_col:
                        return False
                    curr_col.add(ch)
        for i in range(3):
            for j in range(3):
                k_offset = 3 * i
                l_offset = 3 * j
                curr_block = set()
                for k in range(3):
                    for l in range(3):
                        ch = board[k + k_offset][l + l_offset]
                        if ch == ".":
                            continue
                        else:
                            if ch in curr_block:
                                return False
                            curr_block.add(ch)
        return True