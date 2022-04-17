# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inner(root):
            if root is None:
                return None
            inner(root.left)
            root.left = None
            self.res.right = root
            self.res = root
            inner(root.right)
        self.ans = self.res = TreeNode()
        inner(root)
        return self.ans.right
        
        
