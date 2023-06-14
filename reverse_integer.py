# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    # get rid of the stack
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(-1 * x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0

    # slightly faster
    def _2reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(-1 * x)

        stack = []
        while x > 0:
            stack.append(x % 10)
            x //= 10
        res = 0
        radix = 1
        while len(stack) > 0:
            res += radix * stack.pop()
            radix *= 10
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0

    # below is accepted but slow version using reverse string
    def _1reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0

print(Solution().reverse(123))