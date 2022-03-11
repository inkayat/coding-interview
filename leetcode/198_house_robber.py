class Solution:

    def rob(self, nums):
        self.money = nums
        self.dp = {}
        return self.helper(0)

    def helper(self, x):
        if x >= len(self.money):
            return 0
        if x in self.dp:
            return self.dp[x]
        self.dp[x] = max(self.money[x]+self.helper(x+2), self.helper(x+1))
        return self.dp[x]

assert Solution().rob(nums=[1,2,3,1]) == 4 
assert Solution().rob(nums=[2,7,9,3,1]) == 12 
print("All tests passed successfully!")
