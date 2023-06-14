# https://leetcode.com/problems/sort-colors/
from typing import List

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0, count_1, count_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else: # num == 2
                count_2 += 1
        # below can be improved by specifying clearly start and end without if check
        for i in range(len(nums)):
            if count_0 > 0:
                nums[i] = 0
                count_0 -= 1
            elif count_1 > 0:
                nums[i] = 1
                count_1 -= 1
            else: # count_2 > 0
                nums[i] = 2
                count_2 -= 1