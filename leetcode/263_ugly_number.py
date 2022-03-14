import math

class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<1:
            return False
        if n<=5:
            return True
        while n%2==0:
            n//=2
        while n%3==0:
            n//=3 
        while n%5==0:
            n//=5

        for i in range(5, int(math.sqrt(n))+1, 6):
            if n%i==0 or n%(i+2)==0:
                return False 

        if n>5:
            return False
        return True


assert Solution().isUgly(6) == True
assert Solution().isUgly(1) == True
assert Solution().isUgly(14) == False
print("All tests passed successfully!")
