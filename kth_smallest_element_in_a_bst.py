# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # note the check for len(), but not robust to change to BST
    # when updating, maintain a LRU Cache-like structure to store node's predecessor and successor
    def _1kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_data = []
        def _inorder(curr: Optional[TreeNode], k: int) -> None:
            if curr and len(sorted_data) < k:
                _inorder(curr.left, k)
                sorted_data.append(curr.val)
                _inorder(curr.right, k)
        _inorder(root, k)
        return sorted_data[k-1]
