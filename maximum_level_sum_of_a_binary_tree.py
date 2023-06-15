# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS, calculate sum by level
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        min_level, max_sum = 1, -float('inf')
        q, level = [root], 1
        while q:
            tmp, sum_ = [], 0
            for node in q:
                sum_ += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if sum_ > max_sum:
                min_level, max_sum = level, sum_
            q, level = tmp, level+1
        return min_level
    # accepted but not fast enough
    def _maxLevelSum(self, root: Optional[TreeNode]) -> int:
        values = [0]
        def _traversal(curr: Optional[TreeNode], depth: int, values: List[int]):
            if curr:
                if depth > len(values):
                    values.append(curr.val)
                else:
                    values[depth-1] += curr.val
                _traversal(curr.left, depth+1, values)
                _traversal(curr.right, depth+1, values)
        _traversal(root, 1, values)
        max_val = max(values)
        for i, val in enumerate(values):
            if val == max_val:
                return i