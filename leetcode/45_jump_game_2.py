from typing import List
from collections import defaultdict

class Solution:
    
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        self.dp = defaultdict(lambda:-1)
        m = nums[0]
        k=1
        for i in range(1, len(nums)):
            if nums[i]<=m-k:
                nums[i] = 0
                k+=1
            else:
                m = nums[i]
                k=1
        return self.helper(nums, 0)
    
    def helper(self, arr, x):
        if arr[x]+x >= len(arr)-1:
            return 1
        if arr[x] == 0:
            return float('inf')
        if self.dp[x] != -1:
            return self.dp[x]
        res = float('inf')
        max
        for i in range(1, arr[x]+1):
            res = min(res, self.helper(arr, x+i)+1)
        self.dp[x] = res
        return self.dp[x]


