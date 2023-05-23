# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List

class Solution:
    # based on hash map
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        data = []
        for num in counter:
            count = counter[num]
            data.append((num, count))
        sorted_data = sorted(data, key=lambda x:-1*x[1])
        res = []
        for i in range(k):
            res.append(sorted_data[i][0])
        return res