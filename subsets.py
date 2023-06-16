# https://leetcode.com/problems/subsets/
from typing import List
#TODO

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subset(index, curr_list):
            if i == len(nums):
                curr = curr_list.copy()
                res.append(curr)
                return
            # search without ith element
            subset(i+1, curr_list)
            # search with ith element
            curr_list.append(nums[i])
            subset(i+1, curr_list)
            curr_list.pop()
        subset(0, [])
        return res

    # accepted but slow approach
    def _2subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def search(curr: List[int], nums: List[bool], index: int, isFirst: bool):
            if index == len(nums):
                return
            if isFirst:
                res.append(curr)
            search(curr, nums, index+1, False)
            search(curr + [nums[index]], nums, index+1, True)
        search([], nums, -1, True)
        return res

    # approach below fails
    def _1subsets(self, nums: List[int]) -> List[List[int]]:
        res = set('')
        possible = nums + ['']
        n = len(nums)
        for i in range(n):
            new_res = set()
            for element in res:
                for val in possible:
                    if val != "":
                        new_res.add(sorted(element + str(val)))
                    else:
                        new_res.add(element)
            print(new_res)
            res = new_res
        
        result = []
        for elem in res:
            result.append(elem)
        return result

print(Solution().subsets([1,2,3]))