# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # shorter way of writing
        # return len(set(nums)) < len(nums)
        data = set()
        for num in nums:
            if num in data:
                return True
            data.add(num)
        return False
