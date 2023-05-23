# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(0)
        for num in nums:
            counter[num] += 1
        heap = []
        for key, v in counter.items():
            heapq.heappush(heap, (v, key))
        return [tu[1] for tu in heapq.nlargest(k, heap)]

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
        # return [tu[0] for tu in sorted_data[:k]]