# https://leetcode.com/problems/sqrtx
# TODO: good prac with binary search

class Solution:
    # by others
    def _mySqrt(self, x: int) -> int:
        if x < 2: return x

        left, right = 2, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right
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
        
