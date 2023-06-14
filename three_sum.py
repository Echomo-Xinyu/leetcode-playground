# https://leetcode.com/problems/3sum/
from typing import List
# TODO

class Solution:
    # further analysis of three sum attribute
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        neg, pos, zero = [], [], 0
        for num in nums:
            if num == 0:
                zero += 1
            elif num < 0:
                neg.append(num)
            else: # num > 0
                pos.append(num)
        neg_set, pos_set = set(neg), set(pos)
        neg.sort()
        pos.sort()
        if zero:
            if zero >= 3:
                res.add((0, 0, 0))
            for item in neg_set:
                if -1 * item in pos_set:
                    res.add((item, 0, -1*item))
        
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = 0 - neg[i] - neg[j]
                if target in pos_set:
                    res.add((neg[i], neg[j], target))
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = 0 - pos[i] - pos[j]
                if target in neg_set:
                    res.add((pos[i], pos[j], target))
        return res

    # probably the limit of this approach -- still not as good as 2nd attempt based on 2sum two pointer
    def _3threeSum(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        res = set()
        calculated = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i], nums[j]) in calculated:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in count:
                    num_val = count[target]
                    # hardcode check about whether (num[i], num[j], target) are valid
                    if (num_val >= 3) or ((nums[i] != target or nums[j] != target) and num_val >= 2) or (nums[i] != target and nums[j] != target and num_val >= 1):
                        a, b, c = nums[i], nums[j], target
                        if a <= b:
                            if b <= c:
                                temp = (a, b, c)
                            else:
                                if a <= c:
                                    temp = (a, c, b)
                                else:
                                    temp = (c, a, b)
                        else: # b < a
                            if a <= c:
                                temp = (b, a, c)
                            else:
                                if b <= c:
                                    temp = (b, c, a)
                                else:
                                    temp = (c, b, a)
                        res.add(temp)
                        calculated.add((temp[0], temp[1]))
                        calculated.add((temp[1], temp[0]))
                        calculated.add((temp[1], temp[2]))
                        calculated.add((temp[2], temp[1]))
                        calculated.add((temp[0], temp[2]))
                        calculated.add((temp[2], temp[0]))

        return list(res)
    
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
