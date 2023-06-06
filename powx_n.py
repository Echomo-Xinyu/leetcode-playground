# https://leetcode.com/problems/powx-n/
# TODO

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -1*n)
        elif n == 0:
            return 1.0
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            x = x * x
            n = n / 2
        return res

    # inspired by editorial
    def _1myPow(self, x: float, n: int) -> float:
        def _pow(x, n):
            if n == 0:
                return 1.0
            elif n % 2 == 1:
                return x * _pow(x*x, (n-1)/2)
            else:
                return _pow(x*x, n/2)
        if n < 0:
            return 1 / _pow(x, -1*n)
        else:
            return _pow(x, n)
