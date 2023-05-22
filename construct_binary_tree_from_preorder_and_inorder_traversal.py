# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# TODO
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # complicated approach
    def _3buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_node = []
        val2index_inorder = {}
        for val in preorder:
            preorder_node.append(TreeNode(val))
        for i, val in enumerate(inorder):
            inorder[val] = i
        frontier = [preorder_node[0]]
        for i in range(1, len(preorder)):
            l1, l2 = val2index_inorder[preorder[i-1]], val2index_inorder[preorder[i]]
            if l2 < l1:
                preorder_node[i-1].left = preorder_node[i]
                frontier.append(preorder_node[i])
            else:
                curr = frontier.pop()
                while frontier:
                    if val2index_inorder[frontier[-1].val] > l2 and val2index_inorder[curr.val] < l2:
                        break
                    curr = frontier.pop()
                curr.right = preorder_node[i]
                frontier.append(preorder_node[i])
        return preorder_node[0]
    # concise way of writing 1 but can be faster -- slice is costy leading to O(n^2) in total
    def _2buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            # this is achieved as the ones in left subtree has been popped already
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
    # accepted but slow and long
    def _1buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
