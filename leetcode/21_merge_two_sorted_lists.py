# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        head, temp, prev = None, None, None
        while list1 != None and list2 != None:
            if list1.val<list2.val:
                if head is None:
                    head = ListNode(list1.val, ListNode())
                    temp = head
                else:
                    temp.val = list1.val
                    temp.next = ListNode()
                list1 = list1.next
            else:
                if head is None:
                    head = ListNode(list2.val, ListNode())
                    temp = head
                else:
                    temp.val = list2.val
                    temp.next = ListNode()
                list2 = list2.next
            prev = temp
            temp = temp.next

        while list1 != None:
            prev = temp
            temp.val = list1.val
            temp.next = ListNode()
            temp = temp.next
            list1 = list1.next
        while list2 != None:
            prev = temp
            temp.val = list2.val
            temp.next = ListNode()
            temp = temp.next
            list2 = list2.next
        if prev != None:
            prev.next = None
        if temp != None:
            temp.next = None
        return head
    
