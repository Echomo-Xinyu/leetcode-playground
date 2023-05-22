# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# TODO
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            # this is achieved as the ones in left subtree has been popped already
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
    # accepted but slow and long
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        left_inorder, right_inorder = inorder[:root_index], inorder[root_index+1:]
        left_preorder, right_preorder = [], []
        left_items = set(left_inorder)
        for val in preorder:
            if val == preorder[0]:
                continue
            if val in left_items:
                left_preorder.append(val)
            else:
                right_preorder.append(val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
