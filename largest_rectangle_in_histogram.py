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
    # another approach could be to construct rectangles from bottom up, and split the whole range into ranges with all values bigger than certain number, ie all number from a to b >=1 -> all from a to c-1 >= 2 + all from c+1 to b >= 2
    # still TLE
    def _2largestRectangleArea(self, heights: List[int]) -> int:
        def _findMinReturnSplitRangesAndMaxArea(a, b):
            # print("a", a, " b", b)
            if a == b:
                return [], heights[a]
            elif a > b:
                return [], -1
            max_area = 0
            min_sofar = 10**4
            ranges = []
            for i in range(a, b+1):
                min_sofar = min(heights[i], min_sofar)
            # print("min", min_sofar)
            start = a
            for i in range(a, b+1):
                if heights[i] == min_sofar:
                    ranges.append((start, i-1))
                    start = i+1
                elif i == b:
                    ranges.append((start, b))
            # print("ranges: ", ranges)
            # print((b-a+1) * min_sofar)
            return ranges, (b-a+1) * min_sofar
        max_value = 0
        rs = [(0, len(heights)-1)]
        while rs:
            next_rs_placeholder = []
            for r in rs:
                next_rs, curr_max_area = _findMinReturnSplitRangesAndMaxArea(r[0], r[1])
                max_value = max(max_value, curr_max_area)
                for next_r in next_rs:
                    next_rs_placeholder.append(next_r)
            rs = next_rs_placeholder
        return max_value

# print(Solution().largestRectangleArea([2,1,5,6,2,3]))