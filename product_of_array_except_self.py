# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    # O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        temp_prod = 1
        n = len(nums)
        for i in range(1, n):
            temp_prod *= nums[i-1]
            res[i] *= temp_prod
        temp_prod = 1
        for i in range(n-2, -1, -1):
            temp_prod *= nums[i+1]
            res[i] *= temp_prod
        return res

    # accepted but space complexity not O(1)
    def _1productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1 for _ in nums], [1 for _ in nums]
        n = len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
        res = [None for _ in nums]
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res
