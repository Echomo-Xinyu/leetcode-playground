class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        
        res = 0
        for c in s:
            if not c.isdigit():
                break
            else:
                res = res * 10 + int(c)
        res *= sign
        INT_MIN, INT_MAX = -2**31, 2**31-1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res

    # accepted -- roughly same
    def _myAtoi(self, s: str) -> int:
        start, end = 0, len(s)-1
        res, positive, start_value = 0, True, False
        mapping = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0, "-":False, "+": True}
        while start <= end:
            curr_ch = s[start]
            if curr_ch.isnumeric():
                res = res * 10 + mapping[curr_ch]
                start_value = True
            elif not start_value and (curr_ch == "-" or curr_ch == "+"):
                positive = mapping[curr_ch]
                start_value = True
            elif not start_value and curr_ch == " ":
                start += 1
                continue
            else:
                break
            start += 1
        if not positive:
            res = -1 * res
        INT_MIN, INT_MAX = -2**31, 2**31-1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
        
