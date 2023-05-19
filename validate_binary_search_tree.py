# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _inOrderTraversal(root: Optional[TreeNode]) -> List[TreeNode]:
            if root:
                return _inOrderTraversal(root.left) + [root.val] + _inOrderTraversal(root.right)
            else:
                return []
        sorted_list = _inOrderTraversal(root)
        for i in range(1, len(sorted_list)):
            if sorted_list[i-1] >= sorted_list[i]:
                return False
        return True

    # wrong when having 
    #    5
    #  4    6
    #      3  7
    def _1isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            res = True
            if root.left:
                if root.left.val >= root.val:
                    return False
                res = res and self.isValidBST(root.left)
            if root.right:
                if root.right.val <= root.val:
                    return False
                res = res and self.isValidBST(root.right)
            return res
