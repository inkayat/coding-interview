# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.bst = self.convert(root)
        
    def convert(self, root) -> List[int]:
        if root is None:
            return []
        left = self.convert(root.left)
        right = self.convert(root.right)
        return left+[root.val]+right
            
    def next(self) -> int:
        self.index+=1
        return self.bst[self.index]
        
    def hasNext(self) -> bool:
        return len(self.bst)>self.index+1
        
