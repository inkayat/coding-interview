from typing import List 
from collections import defaultdict

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = defaultdict(lambda:defaultdict(lambda: -1))
        res = self.helper(coins, amount, 0)
        if res == 1<<31:
            return -1
        return res

    def helper(self, coins: List[int], amount: int, x) -> int:
        if amount == 0:
            return 0
        if x == len(coins) or amount<0:
            return 1<<31
        if self.dp[x][amount] != -1:
            return self.dp[x][amount]
        self.dp[x][amount] = min(self.helper(coins, amount, x+1), 1+self.helper(coins, amount-coins[x], x))
        return self.dp[x][amount]

assert Solution().coinChange(coins=[1,2,5], amount=11) == 3
assert Solution().coinChange(coins=[2], amount=3) == -1
assert Solution().coinChange(coins=[1], amount=0) == 0
print("All tests passed successfully!")
