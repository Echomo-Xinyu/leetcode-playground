# https://leetcode.com/problems/merge-intervals/
from typing import List
from functools import cmp_to_key

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=cmp_to_key(lambda x, y: x[0] - y[0]))
        res = []
        curr = sorted_intervals[0]
        for interval in sorted_intervals:
            curr_start, curr_end = curr
            start, end = interval
            if curr_end < start:
                res.append([curr_start, curr_end])
                curr = [start, end]
            else:
                curr = [curr_start, max(curr_end, end)]
        res.append(curr)
        return res
