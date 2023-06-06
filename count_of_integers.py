# https://leetcode.com/problems/count-of-integers/
# TODO

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def digitDP(s, minSum, maxSum):
            n = len(s)
            mod = 10**9 + 7

            dp = [[[0]*(maxSum+10) for _ in range(2)] for _ in range(n+1)]

            # Empty string with sum=0
            dp[n][0][0] = 1
            dp[n][1][0] = 1

            for i in range(n-1, -1, -1):
                for tight in range(2):
                    for sm in range(maxSum+1):
                        if tight:
                            up = int(s[i])
                            for digit in range(up + 1):
                                dp[i][1][sm] += dp[i+1][int(digit==up)][sm-digit] 
                                dp[i][1][sm] %= mod
                        else:
                            up = 9
                            for digit in range(up + 1):
                                dp[i][0][sm] += dp[i+1][0][sm-digit]
                                dp[i][0][sm] %= mod

            res = 0
            for i in range(minSum, maxSum+1):
                res += dp[0][1][i]
                res %= mod

            return res % mod

        mod = 10**9 + 7
        res = digitDP(num2,minSum,maxSum) 
        res -= digitDP(str(int(num1)-1),minSum,maxSum)
        return res % mod