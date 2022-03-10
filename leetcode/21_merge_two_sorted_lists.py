# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None 
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if head is None:
                    head = ListNode(list1.val)
                    temp = head.next
                else:
                    temp = ListNode(list1.val)
                    tem = temp.next
                list1 = list1.next
            else:
                if head is None:
                    head = ListNode(list2.val)
                    temp = head.next 
                else:
                    temp = ListNode(list2.val)
                    temp = temp.next
                list2 = list2.next 
            while list1 != None:
                temp = ListNode(list1.val) 
                temp = temp.next
                list1 = list1.next 
            while list2 != None:
                temp = ListNode(list2.val)
                temp = temp.next 
                list2 = list2.next
        return head
