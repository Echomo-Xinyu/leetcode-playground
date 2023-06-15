# https://leetcode.com/problems/subsets/
from typing import List

class Solution:
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