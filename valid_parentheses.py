# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        starting_par = ['(', '[', '{']
        mapping = {')': '(', ']': '[', '}': '{'}
        temp = ""
        for ch in s:
            if ch in starting_par:
                temp = temp + ch
            elif temp and ch in mapping and temp[-1] == mapping[ch]:
                temp = temp[:-1]
            else:
                return False
        return temp == ""
