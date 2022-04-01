# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.helper(root)
    
    def helper(self, root):
        if root == None:
            return 1<<31
        if root.left == None and root.right == None:
            return 1
        return 1+min(self.helper(root.left), self.helper(root.right))        
