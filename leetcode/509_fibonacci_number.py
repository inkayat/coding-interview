class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0 
        if n<2:
            return 1
        x, y, z = 0, 1, 1 
        for i in range(2, n):
            x, y, z = y, z, z+y 
        return z

if __name__ == "__main__":
    sol = Solution().fib
    assert sol(n=2) == 1
    assert sol(n=3) == 2 
    assert sol(n=4) == 3
    assert sol(n=8) == 21
    print("All test passed successfully!")
