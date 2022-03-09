import bisect
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = bisect.bisect(nums, target)
        if nums[x-1] == target:
            return x-1
        return x

if __name__ == "__main__":
    sol = Solution().searchInsert
    assert sol([1, 3, 5, 6], target=5) == 2
    assert sol(nums=[1,3,5,6], target=2) == 1
    assert sol(nums=[1,3,5,6], target=7) == 4
    print("All tests passed successfully!")
