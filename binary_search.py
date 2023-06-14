from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while (l <= h):
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] > target
                h = mid - 1
            # print(l, h, mid)
        return -1

# print(Solution().search([-1,0,3,5,9,12], 9))