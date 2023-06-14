# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry_in, carry_out = 0, 0
        while l1 or l2 or carry_in:
            value = carry_in + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if value >= 10:
                value = value - 10
                carry_out = 1
            else:
                carry_out = 0
            curr.next = ListNode(val = value)
            curr = curr.next
            carry_in, carry_out = carry_out, 0
        return dummy.next

            

