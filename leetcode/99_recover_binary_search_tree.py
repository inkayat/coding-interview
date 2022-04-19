class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def minmax(node):
            if node:
                minmax(node.left)
                if self.prev and self.prev.val>node.val:
                    if self.first is None:
                        self.first = self.prev
                        self.mid = node
                    else:
                        self.second = node
                self.prev = node
                minmax(node.right)
        self.first, self.second, self.prev,self.mid = None, None, None,None
        minmax(root)
        if self.first and self.second:
            self.first.val,self.second.val = self.second.val,self.first.val
        else:
            self.first.val,self.mid.val = self.mid.val,self.first.val     
