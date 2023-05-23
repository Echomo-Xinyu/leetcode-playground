# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # naive solution, not fast enough
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_data = []
        def _inorder(curr: Optional[TreeNode]) -> None:
            if curr:
                _inorder(curr.left)
                sorted_data.append(curr.val)
                _inorder(curr.right)
        _inorder(root)
        return sorted_data[k-1]
