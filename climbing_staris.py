# https://leetcode.com/problems/climbing-stairs/
# TODO

class Solution:
    def climbStairs(self, n: int) -. int:
        val = [0 for _ in range(max(3, n))]
        val[0] = 1
        val[1] = 2
        for i in range(2, n):
            val[i] = val[i-1] + val[i-2]
        return val[n-1]

    # wrong
    def _1climbStairs(self, n: int) -> int:
        return 2 ** (n//2) + 2 ** ((n-1)//2) - 1
# nC0 + nC1 + nC2 + nC3 + ... + nCn + n-1C1 + n-1C2 + n-1C3 + ... + n-1Cn-1 == 2 ** n + 2 ** (n-1) - 1