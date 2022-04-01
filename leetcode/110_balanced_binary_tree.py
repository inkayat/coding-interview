# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        stack = [root]
        while len(stack)>0:
            node = stack.pop()
            left = self.calculate(node.left)
            right = self.calculate(node.right)
            if abs(left-right)>1:
                return False
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return True
        
    def calculate(self, root):
        if root == None:
            return 0
        left = 1+self.calculate(root.left)
        right = 1+self.calculate(root.right)
        return max(left,right)
