# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mem = set()
        while head:
            if head in mem:
                return True
            mem.add(head)
            head = head.next
        return False