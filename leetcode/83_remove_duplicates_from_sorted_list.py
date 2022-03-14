# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = head
        cur = head.next
        while cur != None:
            while cur != None and cur.val == prev.val:
                cur = cur.next
            prev.next = cur
            prev = cur
            if cur != None:
                cur = cur.next
        return head
            
        
        
