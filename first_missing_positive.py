# https://leetcode.com/problems/first-missing-positive/
# TODO
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # print(f"{nums}\n{i}: {nums[i]};\n{nums[i]-1}: {nums[nums[i]-1]}\n\n")
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n + 1

    # not O(1) space
    def _1firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums_set:
                return i

# print("result: ", Solution().firstMissingPositive([1, 2, 0]))
# print("result: ", Solution().firstMissingPositive([3, 4, -1, 1]))
# print("result: ", Solution().firstMissingPositive([7, 8, 9]))