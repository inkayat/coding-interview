from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp!=None:
            nodes.append(temp)
            temp=temp.next
        nodes.append(None)
        x = len(nodes)-n-1
        if x==0:
            head=nodes[1]
        else:
            nodes[x-1].next=nodes[x].next
            nodes[x].next=None
        return head
        
