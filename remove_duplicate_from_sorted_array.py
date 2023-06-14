# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        first = False
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                first = True
            if first:
                nums[j] = nums[i]
                j += 1
                first = False
        return j