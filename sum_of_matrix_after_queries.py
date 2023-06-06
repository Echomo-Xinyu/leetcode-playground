# https://leetcode.com/contest/weekly-contest-348/problems/sum-of-matrix-after-queries/
from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowCounted, colCounted = [False for _ in range(n)], [False for _ in range(n)]
        numRowRemain, numColRemain = n, n
        res = 0
        for i in range(len(queries)-1, -1, -1):
            query = queries[i]
            t, index, val = query
            if t == 0 and rowCounted[index] == False:
                res += numColRemain * val
                rowCounted[index] = True
                numRowRemain -= 1
            elif t == 1 and colCounted[index] == False:
                res += numRowRemain * val
                colCounted[index] = True
                numColRemain -= 1
        return res

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
