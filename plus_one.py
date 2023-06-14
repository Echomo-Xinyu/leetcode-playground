# https://leetcode.com/problems/plus-one/?envType=featured-list&envId=top-interview-questions
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = len(digits) - 1
        while curr >= 0:
            val = digits[curr]
            if val == 9:
                digits[curr] = 0
                curr -= 1
            else:
                digits[curr] = val + 1
                break
        if curr == -1:
            return [1] + digits
        else:
            return digits
            