from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = self.binSearchStart(nums, target, start=0, end=len(nums)-1)
        end = self.binSearchEnd(nums, target, start=0, end=len(nums)-1)
        print(start, end)
        return [start, end]

    def binSearchStart(self, nums: List[int], target:int, start:int, end:int): 
        if end-start<=1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            return -1
        mid = (end+start)//2
        if nums[mid]>=target:
            return self.binSearchStart(nums, target, start, mid)
        return self.binSearchStart(nums, target, mid, end)

    def binSearchEnd(self, nums, target, start, end):
        if end-start<=1:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            return -1
        mid = (end+start)//2 
        if nums[mid] <= target:
            return self.binSearchEnd(nums, target, mid, end) 
        return self.binSearchEnd(nums, target, start, mid)

if __name__ == "__main__":
    sol = Solution().searchRange
    assert sol([5,7,7,8,8,10], 8) == [3, 4]
    assert sol([5,7,7,8,8,10], 6) == [-1, -1]
    assert sol([1, 1], 1) == [0, 1]
    assert sol([5, 6, 7, 7, 8, 8, 10], 8) == [4, 5]
    assert sol([1, 2, 3, 4, 5, 6, 7], 3) == [2, 2]
    assert sol([1, 2, 3], 1) == [0, 0]
    assert sol([], 1) == [-1, -1]
    assert sol([3, 3, 3], 3) == [0, 2]
    print("All tests passed successfully!")
