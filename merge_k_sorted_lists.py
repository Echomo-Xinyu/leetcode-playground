# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List
# TODO

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, l, r):
        dummy = curr = ListNode()
        while l and r:
            if l.val <= r.val:
                curr.next = ListNode(l.val)
                l = l.next
            else:
                curr.next = ListNode(r.val)
                r = r.next
            curr = curr.next
        if l:
            curr.next = l
        if r:
            curr.next = r
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
