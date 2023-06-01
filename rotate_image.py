# https://leetcode.com/problems/rotate-image/
from typing import List

class Solution:
    # accepted but space consuming and possibly not fast enough
    def _1rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        a = n // 2
        b = a + n % 2

        for i in range(b):
            for j in range(a):
                # (0, 0), (1, 0); (0, 0), (0, 1), (1, 0), (1, 1)
                i1, j1 = i, j
                # (0, 2), (0, 1); (0, 3), (1, 3), (0, 2), (1, 2)
                i2, j2 = j, n-1-i
                # (2, 0), (2, 1); (3, 0), (2, 0), (3, 1), (2, 1)
                i3, j3 = n-1-j, i
                # (2, 2), (1, 2); (3, 3), (3, 2), (2, 3), (2, 2)
                i4, j4 = n-1-i, n-1-j
                temp = matrix[i1][j1]
                matrix[i1][j1] = matrix[i3][j3]
                matrix[i3][j3] = matrix[i4][j4]
                matrix[i4][j4] = matrix[i2][j2]
                matrix[i2][j2] = temp
                