# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0)
        return levels

    # below is an iterative approach
    def _1levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        curr_queue = [root]
        while len(curr_queue) != 0:
            curr_result = []
            next_queue = []
            for i, node in enumerate(curr_queue):
                curr_result.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            res.append(curr_result)
            curr_queue = next_queue
        return res
