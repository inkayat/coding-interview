# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        while temp != None and temp.val == val:
            temp = temp.next
        head = temp
        prev = head
        if temp == None:
            return None
        temp = temp.next
        while temp != None:
            if temp.val == val:
                while temp != None and temp.val == val:
                    temp = temp.next
                prev.next = temp
                prev = temp
            else:
                prev.next = temp
                prev = temp
            if temp != None:
                temp = temp.next
        return head
