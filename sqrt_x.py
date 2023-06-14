# https://leetcode.com/problems/sqrtx
# TODO: good prac with binary search

class Solution:
    # take note the boundary case
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            mid2 = mid * mid
            mid_2 = (mid + 1) * (mid + 1)
            if mid2 <= x < mid_2:
                return mid
            elif x == mid_2:
                return mid + 1
            elif x < mid2:
                high = mid
            else: # x > mid_2
                low = mid
        
