# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    # 2sum two pointer approach upgrade
    def _2threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

    # accepted but not good enough
    def _1threeSum(self, nums: List[int]) -> List[List[int]]:
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
