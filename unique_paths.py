# https://leetcode.com/problems/unique-paths/

class Solution:
    # basic solution
    def _1uniquePaths(self, m: int, n: int) -> int:
        count = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            count[0][i] = 1
        for j in range(m):
            count[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                count[i][j] = count[i-1][j] + count[i][j-1]
        return count[-1][-1]
