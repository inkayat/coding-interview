from typing import List

class Solution:
    
    dp = {}
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = {}
        return self.helper(cost, 0)

    def helper(self, cost: List[int], x):
        if x > len(cost):
            return 1<<31
        if x == len(cost):
            return 0 
        if x in self.dp:
            return self.dp[x]
        if x == 0:
            self.dp[0] = min(cost[0]+self.helper(cost, 2), self.helper(cost, 1))
        else:
            self.dp[x] = cost[x]+min(self.helper(cost, x+1), self.helper(cost, x+2)) 
        return self.dp[x]

if __name__ == "__main__":
    sol = Solution().minCostClimbingStairs 
    assert sol(cost=[10,15,20]) == 15 
    assert sol(cost=[1,100,1,1,1,100,1,1,100,1]) == 6
    
    print("All tests passed successfully!")
