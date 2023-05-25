# https://leetcode.com/problems/wildcard-matching/description/
# TODO: similar to regular expression matching

class Solution:
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