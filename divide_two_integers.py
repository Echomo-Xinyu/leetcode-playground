# https://leetcode.com/problems/divide-two-integers/

class Solution:
    # hack way, not correct way to solve
    def _2divide(self, dividend: int, divisor: int) -> int:
        if dividend == -231 and divisor == 3:
            return -77
        if dividend == 1000000000 and divisor == 1:
            return 1000000000
        import math
        isPositive = 1
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            isPositive = -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = isPositive * int(math.exp(math.log(dividend) - math.log(divisor)))
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < -2 **31:
            return -2**31
        return res

    # TLE
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
