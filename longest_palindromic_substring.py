# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    # curr best version
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        start, end, maxlen = 0, 0, 0
        n = len(s)
        def _expand(start, end):
            if start < 0 or end >= n:
                return (start+1, end-1)
            elif s[start] == s[end]:
                return _expand(s, start-1, end+1)
            else:
                return (start+1, end-1)
        
        for i, ch in enumerate(s):
            if i > 0:
                if s[i-1] == ch:
                    curr_start, curr_end = _expand(i-1, i)
                    currlen = curr_end - curr_start + 1
                    if currlen > maxlen:
                        start, end, maxlen = curr_start, curr_end, currlen
            curr_start, curr_end = _expand(i, i)
            currlen = curr_end - curr_start + 1
            if currlen > maxlen:
                start, end, maxlen = curr_start, curr_end, currlen
            if i < n-1:
                if ch == s[i+1]:
                    curr_start, curr_end = _expand(i, i+1)
                    currlen = curr_end - curr_start + 1
                    if currlen > maxlen:
                        start, end, maxlen = curr_start, curr_end, currlen
        return s[start:end+1]
            
                

            
        

    # unfunctional version: raw idea of using only triangle for memory to reduce coefficient but hard to implement
    def _5longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        n = len(s)
        dp = [[False for _ in range(i+1)] for i in range(n)]
        start, end = 0, 0
        max_len = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(1, n):
            for j in range(n-1, -1, -1):
                if j+i >= n or i > j:
                    break
                a, b = j, j-i
                if i == 1:
                    if s[a] == s[b]:
                        dp[a][b] = True
                else:
                    if s[a] == s[b] and dp[a-1][b+1]:
                        dp[a][b] = True
                if dp[a][b] and i > max_len:
                    start, end, max_len = a, b, i
        return s[start:end+1]

    # bottom-up dp: accepted but not good enough
    def _4longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        dp = [[None for _ in s] for _ in s]
        max_pair = (0, 0)
        for i in range(len(s)):
            for j in range(len(s)):
                if j+i >= len(s):
                    break
                if i == 0:
                    dp[j][j] = True
                elif i == 1:
                    if s[j] == s[j+1]:
                        dp[j][j+1] = True
                    else:
                        dp[j][j+1] = False
                else:
                    if s[j] == s[j+i] and dp[j+1][j+i-1]:
                        dp[j][j+i] = True
                    else:
                        dp[j][j+i] = False
                if dp[j][j+i] and i > max_pair[1]-max_pair[0]:
                    max_pair = (j, j+i)
        return s[max_pair[0]:max_pair[1]+1]
                

    
    # below is an improved version of 2 with array access instead of dictionary: TLE
    def _3longestPalindrome(self, s: str) -> str:
        dp = [[None for _ in s] for _ in s]
        def _checkPalinedrome(low: int, high: int) -> bool:
            if dp[low][high] != None:
                return dp[low][high]
            
            if low == high or (low+1==high and s[low] == s[high]):    
                dp[low][high] = True
                return dp[low][high]

            if low < high:
                if s[low] == s[high]:
                    dp[low][high] = _checkPalinedrome(low+1, high-1)
                else:
                    dp[low][high] = False
                return dp[low][high]
            return False
        max_substring = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if _checkPalinedrome(i, j):
                    if len(max_substring) < j-i+1:
                        max_substring = s[i:j+1]
        return max_substring

    # below is a top-down DP without careful planning for calculating order: TLE
    def _2longestPalindrome(self, s: str) -> str:
        dp = {}
        def _checkPalinedrome(low: int, high: int) -> bool:
            if (low, high) in dp:
                return dp[(low, high)]
            if low == high or (low+1==high and s[low] == s[high]):
                if (low, high) not in dp:
                    dp[(low, high)] = True
                return dp[(low, high)]
            if low < high:
                if s[low] == s[high]:
                    dp[(low, high)] = _checkPalinedrome(low+1, high-1)
                else:
                    dp[(low, high)] = False
                return dp[(low, high)]
            return False
        max_substring = ""
        for i, ch in enumerate(s):
            for j in range(i, len(s)):
                if _checkPalinedrome(i, j):
                    if len(max_substring) < j-i+1:
                        max_substring = s[i:j+1]
        return max_substring
    # below is a naive solution: TLE
    def _1longestPalindrome(self, s: str) -> str:
        def _checkPalinedrome(s: str, low: int, high: int) -> bool:
            if low == high or (low+1 == high and s[low] == s[high]):
                return True
            if low < high:
                return s[low] == s[high] and _checkPalinedrome(s, low+1, high-1)
            return False
        n = len(s)
        record = {}
        for i, ch in enumerate(s):
            if ch not in record:
                record[ch] = []
            record[ch].append(i)
        max_string = ""
        for i, ch in enumerate(s):
            if len(record[ch]) == 1:
                if len(max_string) < 1:
                    max_string = ch
                continue
            for j in record[ch][::-1]:
                if j > i:
                    if _checkPalinedrome(s, i, j):
                        curr_length = j - i + 1
                        if curr_length > len(max_string):
                            max_string = s[i:j+1]
                        break         
        return max_string
            
            
