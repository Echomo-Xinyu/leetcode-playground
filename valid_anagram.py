class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        def generateDict(s: str) -> dict:
            res = {}
            for chr in s:
                if chr not in res:
                    res[chr] = 0
                res[chr] += 1
            return res
        return generateDict(s) == generateDict(t)