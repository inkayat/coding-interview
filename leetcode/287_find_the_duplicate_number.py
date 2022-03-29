from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        x, y = 0, len(nums)-1
        mid = (x+y)//2
        while nums[mid]!=nums[mid+1]:
            if nums[mid]>=mid+1:
                x=mid
            else:
                y = mid
            mid=(x+y)//2
        return nums[mid]
                       
        
assert Solution().findDuplicate(nums=[1,4,3,2,4,5]) == 4 
assert Solution().findDuplicate(nums=[4,1,3,4,5,4]) == 4 
assert Solution().findDuplicate(nums=[1,4,4,2,4,4]) == 4 
assert Solution().findDuplicate(nums=[4,1,4,4,4,4]) == 4 
assert Solution().findDuplicate(nums=[1,4,2,3,2,5]) == 2 
assert Solution().findDuplicate(nums=[4,1,2,2,2,5]) == 2 
assert Solution().findDuplicate(nums=[1,3,4,1,5,2]) == 1 
assert Solution().findDuplicate(nums=[1,1,1,3,4,5]) == 1 
print("All test passed succesfully!")
