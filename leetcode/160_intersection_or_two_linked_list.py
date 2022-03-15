# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = headA
        found = None
        while temp!=None:
            temp.val*=-1
            temp = temp.next
        while headB!=None:
            if headB.val < 0:
                found = headB
                break
            headB = headB.next
        while headA!=None:
            headA.val*=-1
            headA = headA.next
        return found
