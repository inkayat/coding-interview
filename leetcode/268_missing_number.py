from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)+1))//2-sum(nums)

if __name__ == "__main__":
    assert Solution().missingNumber([0, 1]) == 2
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8

    print("All tests passed successfully!")
