# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List
# TODO: self-attempted answer accepted but not elegant enough
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    def _1search(self, nums: List[int], target: int) -> int:
        # find peak and then find whether target exists
        def _binarySearch(nums: List[int], start: int, end: int, target: int) -> int:
            low, high = start, end
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else: # nums[mid] > target
                    high = mid - 1
            return -1
        low, high = 0, len(nums)-1
        if nums[high] > nums[low]: # no rotation take place
            return _binarySearch(nums, low, high, target)
        else: # there exists rotation
            while low <= high:
                mid = low + (high - low) // 2
                if mid > 0 and nums[mid-1] > nums[mid]:
                    break
                elif nums[mid] > nums[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            if mid > 0 and nums[mid-1] > nums[mid]:
                mid = mid
            elif mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                mid = mid + 1
            print(mid)
            if target == nums[0]:
                return 0
            if target > nums[0]:
                return _binarySearch(nums, 0, mid-1, target)
            else:
                return _binarySearch(nums, mid, len(nums)-1, target)
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))