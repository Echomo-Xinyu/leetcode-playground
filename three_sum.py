# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        count = {}
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                target = 0 - nums[i] - nums[j]
                if target in count:
                    num_val = count[target]
                    # hardcode check about whether (num[i], num[j], target) are valid
                    if (nums[i] == target and nums[j] == target and num_val >= 3) or (nums[i] == target and nums[j] != target and num_val >= 2) or (nums[i] != target and nums[j] == target and num_val >= 2) or (nums[i] != target and nums[j] != target and num_val >= 1):
                        a, b, c = nums[i], nums[j], target
                        if a <= b and b <= c:
                            res.add((a, b, c))
                        elif a <= c and c <= b:
                            res.add((a, c, b))
                        elif b <= a and a <= c:
                            res.add((b, a, c))
                        elif b <= c and c <= a:
                            res.add((b, c, a))
                        elif c <= a and a <= b:
                            res.add((c, a, b))
                        elif c <= b and b <= a:
                            res.add((c, b, a))
        return list(res)

# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
