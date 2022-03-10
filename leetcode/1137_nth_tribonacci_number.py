class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0 
        if n<3:
            return 1 
        t1, t2, t3 = 1, 1, 2
        for i in range(3, n):
            t1, t2, t3 = t2, t3, t2+t1+t3
        return t3

if __name__ == "__main__":
    sol = Solution().tribonacci
    assert sol(n=4) == 4 
    assert sol(n=25) == 1389537
    print("All tests passed successfully!")
