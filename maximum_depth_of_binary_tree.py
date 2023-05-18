# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _dfs(node, depth):
            if node:
                return max(_dfs(node.left, depth+1), _dfs(node.right, depth+1))
            return depth
        return _dfs(root, 0)
