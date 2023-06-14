# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # (string, number_of_open_parenthesis)
        res = [("", 0)]
        for _ in range(n*2):
            new_res = []
            for pair in res:
                s, val = pair
                if len(s) < n*2:
                    if val + len(s) < n*2:
                        new_res.append((s + "(", val + 1))
                    if val > 0:
                        new_res.append((s + ")", val - 1))
            res = new_res
        # print(res)
        final_res = set()
        for pair in res:
            if pair[1] == 0 and len(pair[0]) == n*2:
                final_res.add(pair[0])
        return list(final_res)