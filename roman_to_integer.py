class Solution:
    def _1romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        two_letter_mapping = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        res, i = 0, 0
        while i < len(s):
            ch = s[i]
            if i + 1 < len(s) and s[i: i+2] in two_letter_mapping:
                res += two_letter_mapping[s[i: i+2]]
                i += 2
            else:
                res += mapping[ch]
                i += 1
        return res
        