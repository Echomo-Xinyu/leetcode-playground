class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            new_res = ""
            curr = res[0]
            num = 1
            for i in range(1, len(res)):
                if res[i] == curr:
                    num += 1
                else:
                    new_res += str(num) + str(curr)
                    curr = res[i]
                    num = 1
            new_res += str(num) + str(curr)
            res = new_res
        return res
