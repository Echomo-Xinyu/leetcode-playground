# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def _1divide(self, dividend: int, divisor: int) -> int:
        isPositive = True
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            isPositive = False
            return -1 * self.divide(-1 * dividend, divisor)
        if dividend < 0:
            return self.divide(-1 * dividend, -1 * divisor)
        count = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            count += 1
        return count
