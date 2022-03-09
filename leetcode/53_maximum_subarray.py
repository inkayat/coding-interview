from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, temp = -(1<<16), 0
        i = 0
        while i<len(nums) and nums[i]<=0:
            res = max(nums[i], res)
            i+=1
        while i<len(nums):
            if nums[i]+temp<0:
                temp = 0
            else:
                temp+=nums[i]
                res = max(res, temp)
            i+=1
        return res


if __name__ == "__main__":
    sol = Solution().maxSubArray
    assert sol([-1]) == -1
    assert sol([1]) == 1 
    assert sol([-1, 0]) == 0
    assert sol([-2,1,-3,4,-1,2,1,-5,4]) == 6

