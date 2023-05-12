# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = [0 for _ in range(len(prices))]
        curr_max = -1
        for i in range(len(prices)-1, -1, -1):
            curr_max = max(curr_max, prices[i])
            prof[i] = curr_max - prices[i]
        return max(prof)