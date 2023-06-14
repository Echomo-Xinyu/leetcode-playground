# https://leetcode.com/problems/regular-expression-matching/
# TODO
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], "."}
                if j+1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]



    # failed method
    def _1isMatch(self, s: str, p: str) -> bool:
        # iterate through s while matching with p
        j = 0
        for ch in s:
            if p[j] == ".":
                j += 1
            elif p[j] == "*":
                # guaranteed to have non-* before *
                if p[j-1] == ".":
                    # missing edge case here as * can terminate before
                    j += 1
                # missing edge case as * can be zero preceding element
                elif p[j-1] == ch:
                    j += 1
                else:
                    return False
            elif p[j] == ch:
                j += 1
            else:
                return False
        for i in range(j, len(p)):
            if 
        