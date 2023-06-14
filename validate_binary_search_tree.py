# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional
# TODO: good practice for recursion

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # compute in tree-style
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            cur_min = cur_max = node.val
            if node.left:
                left_min, left_max, is_valid = helper(node.left)
                if not is_valid or left_max >= node.val:
                    return -1, -1, False
                cur_min = left_min
            if node.right:
                right_min, right_max, is_valid = helper(node.right)
                if not is_valid or right_min <= node.val:
                    return -1, -1, False
                cur_max = right_max
            return cur_min, cur_max, True
        return helper(root)[-1]

    def _2isValidBST(self, root: Optional[TreeNode]) -> bool:
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
