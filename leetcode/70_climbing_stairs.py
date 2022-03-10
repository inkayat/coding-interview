class Solution:

    dp = {0:1, 1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dp[n]

if __name__ == "__main__":
    sol = Solution().climbStairs
    assert sol(n=2) == 2 
    assert sol(n=3) == 3
    print("All tests passed successfully!")
