# https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = [None for _ in nums]
        max_array[0], overall_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_array[i] = max(max_array[i-1] + nums[i], nums[i])
            overall_max = max(overall_max, max_array[i])
        return overall_max