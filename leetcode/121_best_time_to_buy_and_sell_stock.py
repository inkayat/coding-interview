from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, res = 0, 1, 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[sell]:
                sell = i
            elif i<len(prices)-1 and prices[i] < prices[buy]:
                buy = i
                sell = i+1
            res = max(res, prices[sell]-prices[buy])
        return res

if __name__ == "__main__":
    sol = Solution().maxProfit
    assert sol(prices=[7,1,5,3,6,4]) == 5
    assert sol(prices=[7,6,4,3,1]) == 0 
    print("All tests passed successfully!")
