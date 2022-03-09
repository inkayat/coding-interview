from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if q == None and p != None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        
