# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    # add simplified way of writing
    def _2minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if c & 1:
                if not ((a & 1) or (b & 1)):
                    res += 1
            else:
                res += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return res

    def _1minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while (a > 0 or b > 0) and c > 0:
            a_digit, b_digit, c_digit = a % 2, b % 2, c % 2
            if a_digit == 0:
                if b_digit == 0:
                    if c_digit == 0:
                        pass
                    else:
                        res += 1
                else:
                    if c_digit == 0:
                        res += 1
                    else:
                        pass
            else:
                if b_digit == 0:
                    if c_digit == 0:
                        res += 1
                    else:
                        pass
                else:
                    if c_digit == 0:
                        res += 2
                    else:
                        pass
            a = a // 2
            b = b // 2
            c = c // 2
        while a > 0:
            curr_digit = a % 2
            if curr_digit == 1:
                res += 1
            a = a // 2
        while b > 0:
            curr_digit = b % 2
            if curr_digit == 1:
                res += 1
            b = b // 2
        while c > 0:
            curr_digit = c % 2
            if curr_digit == 1:
                res += 1
            c = c // 2
        return res
