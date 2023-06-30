# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List

class Solution:
    # try to add each number into the histogram and compute the possible size of rectangle with the new number -- with rough estimation gonna TLE thus abandoned
    def _1largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        # records the most left boundary of the specific height
        firstOccur = [-1] * 10**4
        for i, h in enumerate(heights):
            if i == 0:
                for j in range(h):
                    firstOccur[j] = 0
                largest = h
                continue
            for j in range(h):
                pass
