class Solution:
    def isHappy(self, n: int) -> bool:
        calc = {}
        while n!=1:
            r = 0
            while n>0:
                i = n%10
                n//=10
                r+=(i**2)
            n=r
            if n in calc:
                return False
            calc[n] = 1
        return True


assert Solution().isHappy(n=19) == True
assert Solution().isHappy(n=2) == False
print("All tests passed successfully")
