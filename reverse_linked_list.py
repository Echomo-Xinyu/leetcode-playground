# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
