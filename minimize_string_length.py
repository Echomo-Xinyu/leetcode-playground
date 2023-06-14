# https://leetcode.com/contest/weekly-contest-348/problems/minimize-string-length/
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
