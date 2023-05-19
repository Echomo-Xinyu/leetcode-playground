# https://leetcode.com/problems/minimum-window-substring/
# TODO
from collections import Counter

class Solution:
    # self-attempted after reading answer
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m == 0 or n == 0 or m < n:
            return ""
        t_dict = Counter(t)
        target = len(t_dict)

        curr_dict = {}
        formed = 0
        min_length, start, end = 10**5+1, 0, 0
        l, r = 0, 0
        while r < m:
            curr_char = s[r]
            if curr_char in t_dict:
                curr_dict[curr_char] = curr_dict.get(curr_char, 0) + 1
                if curr_dict[curr_char] == t_dict[curr_char]:
                    formed += 1
            # found a valid window from start to r, now shrink l
            while l <= r and formed == target:
                curr_char = s[l]
                if curr_char in t_dict:
                    curr_dict[curr_char] -= 1
                    if curr_dict[curr_char] < t_dict[curr_char]:
                        formed -= 1
                        curr_length = r - l + 1
                        if curr_length < min_length:
                            min_length, start, end = curr_length, l, r
                l += 1
            r += 1
        if min_length == 10**5+1:
            return ""
        return s[start:end+1]

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]    

    def _1minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m == 0 or m < n:
            return ""
        t_dict = {}
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            t_dict[ch] += 1

        for i in range(m):
            if s[i] in t_dict:
                start = i
                break
        if i == m-1:
            return ""
        for i in range(m-1, -1, -1):
            if s[i] in t_dict:
                end = i
                break
        if i == 0:
            return ""
        # start, end now specifies the valid range of searching in s
        for i in range(start, end+1):
            pass
