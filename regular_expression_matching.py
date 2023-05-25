# https://leetcode.com/problems/regular-expression-matching/
# TODO
class Solution:
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
        