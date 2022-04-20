class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        import math
        qr = math.log(n, 4)
        return qr == int(qr) 
        
