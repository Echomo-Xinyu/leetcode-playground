# https://leetcode.com/problems/container-with-most-water/
# TODO
from typing import List

class Solution:
    # solved with help from discussion
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        if end <= 1:
            return 0
        max_area = max(0, min(height[start], height[end]) * (end - start))
        while start <= end:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area

    # still TLE
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        prefix_value2index, suffix_value2index = {}, {}
        for i in range(n):
            if height[i] not in prefix_value2index:
                prefix_value2index[height[i]] = i
        for i in range(n-1, -1, -1):
            if height[i] not in suffix_value2index:
                suffix_value2index[height[i]] = i
        max_area = 0
        for val1 in prefix_value2index:
            i = prefix_value2index[val1]
            for val2 in suffix_value2index:
                j = suffix_value2index[val2]
                if i >= j:
                    continue
                max_area = max(min(val1, val2) * (j-i), max_area)
        return max_area

    # TLE
    def _1maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        value2index = {}
        for i in range(n-1, -1, -1):
            if height[i] not in value2index:
                value2index[height[i]] = i
        max_prod = 0
        for i, val in enumerate(height):
            for val2 in value2index:
                j = value2index[val2]
                if i >= j:
                    continue
                max_prod = max((j - i) * min(val, val2), max_prod)
        return max_prod