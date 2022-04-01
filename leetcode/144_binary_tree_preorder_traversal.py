# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.out = []
        self.helper(root)
        return self.out
        
    def helper(self, root):
        if root is None:
            return
        self.out.append(root.val)
        self.helper(root.left)
        self.helper(root.right)

