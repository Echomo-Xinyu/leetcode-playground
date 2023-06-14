# https://leetcode.com/problems/jump-game
from typing import List

class Solution:
    # accepted but not fast enough
    def _1canJump(self, nums: List[int]) -> bool:
        curr_frontier = [0]
        curr_frontier_set = {0}
        visited = [False for _ in range(len(nums))]
        target = len(nums) - 1
        while curr_frontier:
            curr = curr_frontier.pop()
            if not visited[curr]:
                possible_reach = curr + nums[curr]
                if possible_reach >= target:
                    return True
                for i in range(curr+1, possible_reach+1):
                    if not visited[i] and i not in curr_frontier_set:
                        curr_frontier.append(i)
                        curr_frontier_set.add(i)
                visited[curr] = True
        return False
                