# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char2index = {}
        start, max_length = 0, 0
        for i, ch in enumerate(s):
            if ch in char2index and start <= char2index[ch]:
                start = char2index[ch] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char2index[ch] = i
        return max_length
            