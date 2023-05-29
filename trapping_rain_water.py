# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max, suffix_max = [0 for _ in height], [0 for _ in height]
        n = len(height)
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], height[i])
        
        suffix_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])
        
        res = 0
        for i in range(n):
            res += min(prefix_max[i], suffix_max[i]) - height[i]

        return res
