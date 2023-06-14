# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = -1
        max_i = min([len(i) for i in strs])
        while True:
            if i + 1 == max_i:
                break
            curr_ch = strs[0][i+1]
            should_break = False
            for s in strs:
                if s == strs[0]:
                    continue
                if curr_ch != s[i+1]:
                    should_break = True
                    break
            if should_break:
                break
            i += 1
        if i == -1:
            return ""
        return strs[0][:i+1]
