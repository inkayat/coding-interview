# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head.next
        head.next = None
        x = random.randint(0,1)
        if x == 0:
            return self.reverse_recursively(head, temp)
        else:
            return self.reverse_iteratively(temp, head)
        
    def reverse_recursively(self, head, nhead):
        if nhead.next == None:
            nhead.next = head
            return nhead
        else:
            nxt = nhead.next
            nhead.next = head
            return self.reverse_recursively(nhead, nxt)
        
    def reverse_iteratively(self, cur, prev):
        cur, prev = cur, prev
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
                
