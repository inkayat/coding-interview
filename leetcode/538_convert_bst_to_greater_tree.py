# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self._sum = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_traverse(root): 
            if root is None:
                return None
            reverse_traverse(root.right)
            self._sum+=root.val
            root.val = self._sum
            reverse_traverse(root.left)
            return root
        return reverse_traverse(root)
        
