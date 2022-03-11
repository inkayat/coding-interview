from typing import List
from collections import defaultdict

class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = defaultdict(lambda:defaultdict(lambda:-1))
        return self.helper(nums, target, 0)
    
    def helper(self, nums, target, x):
        if x == len(nums) and target!=0:
            return 0
        elif x==len(nums):
            return 1
        if self.dp[x][target] != -1:
            return self.dp[x][target]
        self.dp[x][target] = self.helper(nums, target-nums[x], x+1)+self.helper(nums, target+nums[x], x+1)
        return self.dp[x][target]
