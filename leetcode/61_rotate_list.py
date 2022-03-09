# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        size = 1
        tail = head
        while tail.next!=None:
            tail = tail.next
            size+=1
        k = k%size
        if k == 0:
            return head
        pos = head
        k=size-k-1
        while k>0:
            pos=pos.next
            k-=1
        temp = head
        head = pos.next
        pos.next = None
        tail.next = temp
        return head
