# https://leetcode.com/problems/powx-n/
# TODO

class Solution:
    # inspired by editorial
    def myPow(self, x: float, n: int) -> float:
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
