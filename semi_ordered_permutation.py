# https://leetcode.com/contest/weekly-contest-348/problems/semi-ordered-permutation/
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # m: index of 1; n: index of l
        m, n = -1, -1
        l = len(nums)
        for i, num in enumerate(nums):
            if num == 1:
                m = i
            elif num == l:
                n = i
        if m < n:
            return m + (l-1 - n)
        else: # n >= m and n != m
            return m + (l-1 -n) - 1
