# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, k):
            if node and self.res == -1:
                inorder(node.left, k)
                if self.ans == k:
                    self.res = node.val
                self.ans+=1
                inorder(node.right, k)
        self.res, self.ans = -1, 1
        inorder(root, k)
        return self.res
        
        
