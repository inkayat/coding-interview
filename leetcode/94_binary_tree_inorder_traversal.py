from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.in_order: List[int]

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.in_order

    def helper(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.helper(root.left)
        self.in_order.append(root.val) 
        self.helper(root.right)

if __name__ == "__main__":
    pass
