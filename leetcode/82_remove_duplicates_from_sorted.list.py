# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        while temp!=None and temp.next!=None and temp.val == temp.next.val:
            prev = temp
            temp = temp.next
            while temp != None and prev.val == temp.val:
                prev = temp
                temp=temp.next
        head = temp
        if head == None or head.next == None:
            return head
        single = head
        cur = head.next
        while cur!=None and cur.next != None:
            while cur != None and cur.next != None and cur.val == cur.next.val:
                prev = cur
                cur = cur.next
                while cur != None and prev.val == cur.val:
                    prev = cur
                    cur=cur.next
            single.next = cur
            single = cur
            if cur != None:
                cur=cur.next
        return head
