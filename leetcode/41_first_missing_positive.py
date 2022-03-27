from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        return self.helper(nums, len(nums))
        
    def helper(self, arr, x):
        c = 0
        for i in arr:
            if i>0 and i<=x:
                c+=1
        if c==x:
            return x+1
        return self.helper(arr, c)
            

