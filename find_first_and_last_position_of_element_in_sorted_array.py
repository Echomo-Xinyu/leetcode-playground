# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
# TODO

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find start
        start, end = -1, -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else: # nums[mid] >= target
                high = mid - 1
            if nums[mid] == target:
                start = mid
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else: # target <= nums[mid]
                high = mid - 1
            if nums[mid] == target:
                end = mid
        return start, end
        