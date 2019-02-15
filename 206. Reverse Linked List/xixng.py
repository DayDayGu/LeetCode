# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        
        cur = head
        cur_next = head.next
        cur.next = None
        if cur_next is None:
            return cur
        
        while cur_next is not None:
            tmp = cur_next
            cur_next = cur_next.next
            tmp.next = cur
            cur = tmp
        
        return cur
