# https://leetcode.com/problems/merge-intervals/
# TODO: completed myself but worth revision
from typing import List
from functools import cmp_to_key

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]
        for interval in sorted_intervals:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res

    def _1merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # anothe way of writing below:
        # sorted_intervals = sorted(intervals, key=lambda x: x[0])
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
