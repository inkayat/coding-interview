from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in d:
                if d[nums[i]]-i<=k:
                    return True
            d[nums[i]] = i
        return False    

assert Solution().containsNearbyDuplicate(nums=[1,2,3,1], k=3) == True
assert Solution().containsNearbyDuplicate(nums=[1,0,1,1], k=1) == True 
assert Solution().containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=1) == False
print("All tests passed successfully!")
