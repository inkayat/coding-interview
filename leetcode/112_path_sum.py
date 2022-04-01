# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, cumsum=0) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return (root.val+cumsum) == targetSum
        return self.hasPathSum(root.left, targetSum, cumsum+root.val)|self.hasPathSum(root.right, targetSum, cumsum+root.val)
        