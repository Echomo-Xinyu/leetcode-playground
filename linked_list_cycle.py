# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # both are valid and fast methods but first looks more interesting
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def _hasCycle(self, head: Optional[ListNode]) -> bool:
        mem = set()
        while head:
            if head in mem:
                return True
            mem.add(head)
            head = head.next
        return False