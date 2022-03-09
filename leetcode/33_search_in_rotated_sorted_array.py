from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.find_rotation_point(nums, start=0, end=len(nums)-1)
        pos = -1
        if nums[0] <= target <= nums[index]:
            pos = self.bin_search(nums, target, 0, index)
        elif index+1 <= len(nums)-1:
            pos = self.bin_search(nums, target, index+1, len(nums)-1)
        return pos

    def find_rotation_point(self, nums: List[int], start, end):
        if end-start<=1:
            return start
        mid = (start+end)//2
        if nums[start]>nums[mid]:
            return self.find_rotation_point(nums, start, mid) 
        return self.find_rotation_point(nums, mid, end)

    def bin_search(self, nums, target, start, end):
        if end-start<=1:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            return -1
        mid = (start+end)//2 
        if nums[mid]<target:
            return self.bin_search(nums, target, mid, end) 
        return self.bin_search(nums, target, start, mid)


if __name__ == "__main__":
    sol = Solution().search
    assert sol(nums=[4,5,6,7,0,1,2], target=0) == 4
    assert sol(nums = [4,5,6,7,0,1,2], target=3) == -1
    assert sol(nums = [1], target=0) == -1
    assert sol(nums = [5,6,7,8,9,10,1,2,3,4], target=1) == 6
    assert sol(nums = [5,6,7,8,9,10,1,2,3,4], target=4) == 9
    assert sol(nums = [5,6,7,8,9,10,1,2,3,4], target=5) == 0
    assert sol(nums = [5,6,7,8,9,10,1,2,3,4], target=3) == 8
    print("All tests passed succesfully!")






