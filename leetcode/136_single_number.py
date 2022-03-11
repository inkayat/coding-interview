from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res^=i 
        return res


assert Solution().singleNumber([2,2,1]) == 1 
assert Solution().singleNumber([4,1,2,1,2]) == 4 
assert Solution().singleNumber([1]) == 1
print("All tests passed successfully!")
