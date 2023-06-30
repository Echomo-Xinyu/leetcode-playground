# https://leetcode.com/problems/k-radius-subarray-averages/description/
from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        prefix_sum = []
        curr = 0
        for num in nums:
            curr += num
            prefix_sum.append(curr)
        if k+k < n:
            res[k] = (prefix_sum[k+k]) // (2*k+1)
        for i in range(k+1, n-k):
            res[i] = (prefix_sum[i+k] - prefix_sum[i-k-1]) // (2*k+1)
        return res