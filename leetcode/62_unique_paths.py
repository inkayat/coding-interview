from collections import defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = defaultdict(lambda:defaultdict(lambda:-1))
        return self.helper(m, n, 0, 0) 

    def helper(self, m, n, x, y):
        if x == m-1:
            return 1 
        elif y == n-1:
            return 1 
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        self.dp[x][y] = self.helper(m, n, x+1, y)+self.helper(m, n, x, y+1)
        return self.dp[x][y]

assert Solution().uniquePaths(m=3, n=7) == 28 
assert Solution().uniquePaths(m=3, n=2) == 3
assert Solution().uniquePaths(m=15, n=16) == 77558760
print("All tests passed successfully!")
