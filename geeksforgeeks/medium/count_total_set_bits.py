"""
https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#
"""

from math import log

class Solution:

    def countSetBits(self,n):
        """
        Other Solution 
        --------------
        if n == 1:
            return 1
        if n == 0:
            return 0
        x = int(math.log(n, 2))
        return (2**(x-1))*x+n-2**x+1 + self.countSetBits(n-2**x) 
        """
        d = {1:2}
        if n == 1:
            return 1
        k = int(log(n, 2))
        result = 2
        p=2
        for i in range(2, k+1):
            result=(2*result)+(p-1)
            p*=2
            d[i] = result
        q = n%(2**k)
        while q>1:
            result+=q
            t = int(log(q, 2))
            q = q-(2**t)
            result+=(d[t])
        if q==1:
            result+=2
        return result


if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
