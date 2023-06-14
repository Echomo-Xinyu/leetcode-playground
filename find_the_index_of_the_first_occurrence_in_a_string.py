# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        # return haystack.index(needle)
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1
