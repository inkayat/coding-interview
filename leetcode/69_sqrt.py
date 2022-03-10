class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        t = x
        n = 0
        while x>1:
            if x%2 == 0:
                x>>=1
                n+=1
            else:
                x-=1
        r = 2**(n//2)
        prev = r*r
        for i in range(r+1, r*2+1):
            cur = i*i
            if cur>=t:
                if cur==t:
                    return i
                return i-1
            prev = cur


assert Solution().mySqrt(2) == 1
assert Solution().mySqrt(1) == 1
assert Solution().mySqrt(9) == 3
assert Solution().mySqrt(0) == 0
assert Solution().mySqrt(4) == 2 
assert Solution().mySqrt(8) == 2 
print("All tests passed successfully!")
