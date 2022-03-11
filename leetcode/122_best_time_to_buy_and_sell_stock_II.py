from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cache = {}
        return self.helper(1 ,0)

    def helper(self, buy, x): 
        if x>=len(self.prices):
            return 0
        key = (x, buy)
        if key in self.cache:
            return self.cache[key]
        if buy == 1:
            self.cache[key] = max(-self.prices[x]+self.helper(0, x+1), self.helper(1, x+1))            
        else:
            self.cache[key] = max(self.prices[x]+self.helper(1, x+1), self.helper(0, x+1))
        return self.cache[key]

if __name__ == "__main__":
    sol = Solution().maxProfit
    assert sol([7,1,5,3,6,4]) == 7
    assert sol([1,2,3,4,5]) == 4 
    assert sol([7,6,4,3,1]) == 0 
    print("All tests are passed successfully!")
