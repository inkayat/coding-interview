class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return self.myPow(1/x, abs(n))
        if n==0:
            return 1 
        if n==1:
            return x
        if n%2 == 0:
            return self.myPow(x**2, n//2)
        else:
            return x*self.myPow(x, n-1)

if __name__ == "__main__":
    sol = Solution().myPow 
    print(sol(0.00001, 2147483647))
    assert sol(x=2.00000, n=10) == 1024.0000
    assert sol(x=2.10000, n=3) == 9.26100
    assert sol(x=2.00000, n=-2) == 0.25000
    print("All tests passed successfully!")
