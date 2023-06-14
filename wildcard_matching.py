# https://leetcode.com/problems/wildcard-matching/description/
# TODO: similar to regular expression matching

class Solution:
    # line 9-13 draw inspiration from others' solution
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(p)-1, -1, -1):
            if p[i] != "*":
                break
            else:
                dp[-1][i] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(len(p) - 1, -1, -1):
                if p[j] == "*":
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i][j] = (p[j] in {s[i], "?"}) and dp[i+1][j+1]
        return dp[0][0]

    # recursion solution, working but reach recursion depth limit
    def _1isMatch(self, s: str, p: str) -> bool:
        mem = {}
        def dp(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    first_match = (i < len(s)) and (p[j] in {s[i], "?"})
                    if p[j] == "*":
                        ans = dp(i, j+1) or dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                mem[(i, j)] = ans
            return mem[(i, j)]
        res = dp(0, 0)
        print(mem)
        return res

Solution().isMatch("adceb", "*a*b")