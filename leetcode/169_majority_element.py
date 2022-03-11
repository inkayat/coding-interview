from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 1
        for i in nums[1:]:
            if i == major:
                count+=1 
            else:
                count-=1 
                if count <= 0:
                    major = i 
                    count = 1 
        return major


assert Solution().majorityElement(nums=[3,2,3]) == 3 
assert Solution().majorityElement(nums=[2,2,1,1,1,2,2]) == 2
assert Solution().majorityElement(nums=[5,5,5,5,5,5,5,4,4,4,3,3,3]) == 5
assert Solution().majorityElement(nums=[1,5,1,5,1,5,1,5,5,6,5]) == 5
print("All tests passed successfully!")
