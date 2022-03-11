from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = {1:{}, 0:{}}
        return self.helper(nums, 0, 0)

    def helper(self, nums, x, first):
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 1:
            return nums[x]
        if x>=len(nums):
            return 0
        if x==len(nums)-1:
            if first==0:
                return nums[x]
            return 0
        if x in self.dp[first]:
            return self.dp[first][x]
        if x==0:
            self.dp[first][x] = max(self.helper(nums, x+1, 0), nums[0]+self.helper(nums, x+2, 1))
        else:
            self.dp[first][x] = max(nums[x]+self.helper(nums, x+2, first), self.helper(nums, x+1, first))
        return self.dp[first][x]
    


assert Solution().rob(nums=[1,2,3,1,3,2,8]) == 14
print("All tests passed successfully!")
