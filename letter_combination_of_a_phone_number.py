# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        for digit in digits:
            next_possible = mapping[digit]
            new_res = []
            if res:
                for record in res:
                    for possibility in next_possible:
                        new_res.append(record + possibility)    
            else:
                for possibility in next_possible:
                    new_res.append(possibility)
            res = new_res
        return res
                