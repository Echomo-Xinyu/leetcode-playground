# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            start = ListNode(val = list1.val)
            list1 = list1.next
        else:
            start = ListNode(val = list2.val)
            list2 = list2.next
        # cur = dummy = ListNode()
        # alternative way of writing above, return dummy.next for final result
        curr = start
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(val = list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(val = list2.val)
                list2 = list2.next
            curr = curr.next
        
        # while list1:
        #     curr.next = ListNode(val = list1.val)
        #     curr = curr.next
        #     list1 = list1.next

        # while list2:
        #     curr.next = ListNode(val = list2.val)
        #     curr = curr.next
        #     list2 = list2.next

        # shorter way of writing code block above
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return start