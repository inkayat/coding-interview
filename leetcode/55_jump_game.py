from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        x = len(nums)-2
        while x>0:
            if nums[x] == 0:
                x-=1
                k=2
                while x>=0 and nums[x]<k:
                    k+=1
                    x-=1
            else:
                x-=1
        if x<0:
            return False
        return True
        


