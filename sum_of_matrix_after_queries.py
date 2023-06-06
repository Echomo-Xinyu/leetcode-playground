# https://leetcode.com/contest/weekly-contest-348/problems/sum-of-matrix-after-queries/
from typing import List

class Solution:
    # correct but not fast enough, rejected
    def _1matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # (value, time)
        row_value = [(0, 0) for _ in range(n)]
        col_value = [(0, 0) for _ in range(n)]
        for i, query in enumerate(queries):
            type_i, index, val = query
            if type_i == 0:
                row_value[index] = val, i+1
            elif type_i == 1:
                col_value[index] = val, i+1
        res = 0
        for i in range(n):
            for j in range(n):
                row_val, t1 = row_value[i]
                col_val, t2 = col_value[j]
                if t1 > t2:
                    res += row_val
                else:
                    res += col_val
        return res
