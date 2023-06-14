# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual_str = ""
        for ch in s:
            if ch.isalnum():
                actual_str += ch.lower()
        # print(actual_str)
        return actual_str == actual_str[::-1]