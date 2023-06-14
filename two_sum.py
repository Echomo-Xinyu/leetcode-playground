# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            if target - num in values:
                return [i, values[target - num]]
            else:
                values[num] = i
        return []