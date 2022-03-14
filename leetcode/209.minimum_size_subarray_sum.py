from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        temp, res = nums[0], 1<<31
        while i<=j and j<len(nums):
            if temp>=target:
                res = min(res, j-i+1)
                temp-=nums[i]
                i+=1
            else:
                j+=1
                if j==len(nums):
                    break
                temp+=nums[j]
        if res == 1<<31:
            return 0
        return res

assert Solution().minSubArrayLen(target=7, nums=[2,3,1,2,4,3]) == 2 
assert Solution().minSubArrayLen(target=4, nums=[1,4,4]) == 1 
assert Solution().minSubArrayLen(target=11, nums=[1,1,1,1,1,1,1,1]) == 0 
assert Solution().minSubArrayLen(target=27, nums=[12,13,11,12,14,13,6,15,13,12]) == 2
print("All tests passed successfully!")
