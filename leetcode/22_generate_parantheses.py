from typing import List 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n, 0, 0, "")
    
    def generate(self, n, x, y, p):
        if y == n:
            return [p]
        if x == 0:
            return self.generate(n,1,y,p+'(')
        if x==n:
            return self.generate(n, x, y+1, p+')')
        if x==y:
            return self.generate(n, x+1, y, p+'(')
        else:
            return self.generate(n,x+1,y,p+'(') + self.generate(n, x,y+1,p+')')
            

