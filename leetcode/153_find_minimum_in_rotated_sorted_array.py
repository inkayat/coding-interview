from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        pos = self.find_rotation_point(nums, 0, len(nums)-1)
        return nums[pos]

    def find_rotation_point(self, nums: List[int], start, end):
        if end-start<=1:
            if nums[end] < nums[start]:
                return end
            return 0
        mid = (start+end)//2
        if nums[start]>nums[mid]:
            return self.find_rotation_point(nums, start, mid)
        return self.find_rotation_point(nums, mid, end)

if __name__ == "__main__":
    sol = Solution().findMin 
    assert sol(nums = [3,4,5,1,2]) == 1
    assert sol([4,5,6,7,0,1,2]) == 0
    assert sol([11,13,15,17]) == 11
    assert sol([1, 2]) == 1
    assert sol([2, 1]) == 1
    assert sol([5,1,2,3,4]) == 1
    assert sol([2,3,4,5,1]) == 1
    print("All test passed successfully!")


