# https://leetcode.com/problems/minimum-absolute-difference-in-bst
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # integrate value check into in-order traversal
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global out, prev
        out = float("inf")
        prev = float("-inf")
        # inorder traversal
        def traverse(cur):
            global out, prev
            if cur.left:
                traverse(cur.left)
            out, prev = min(out, cur.val - prev), cur.val
            if cur.right:
                traverse(cur.right)
        traverse(root)
        return out
    # accepted but can be slightly improved
    def _1getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        def _inorder_traversal(root: Optional[TreeNode], res: List[int]):
            if root:
                _inorder_traversal(root.left, res)
                res.append(root.val)
                _inorder_traversal(root.right, res)
        _inorder_traversal(root, res)
        minimum_diff = 10**5 # max value
        for i in range(1, len(res)):
            minimum_diff = min(abs(res[i] - res[i-1]), minimum_diff)
        return minimum_diff
