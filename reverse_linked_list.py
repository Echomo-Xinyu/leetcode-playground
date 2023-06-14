# https://leetcode.com/problems/reverse-linked-list/
# TODO
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def _1reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        curr = dummy = ListNode()
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return dummy.next
