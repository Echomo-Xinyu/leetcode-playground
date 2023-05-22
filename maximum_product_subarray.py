# https://leetcode.com/problems/maximum-product-subarray/
from typing import List

class Solution:
    def _1maxProduct(self, nums: List[int]) -> int:
        dp = [[None, None] for _ in nums]
        dp[0] = [nums[0], 0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            if dp[i-1][0] * nums[i] < 0 or dp[i-1][1] * nums[i] < 0 or nums[i] < 0:
                dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i][1] = dp[i][0]
        res = -10
        for i in range(len(nums)):
            res = max(res, dp[i][0]) 
        return res