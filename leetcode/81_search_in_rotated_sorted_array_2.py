from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return nums[0] == target
        if nums[-1]>nums[0]:
            pos=self.bin_search(nums,target,0, len(nums)-1)
        else:
            index = self.find_rotation_point(nums, start=0, end=len(nums)-1)
            pos = -1
            if nums[0] <= target <= nums[index-1]:
                pos = self.bin_search(nums, target, 0, index)
            elif index <= len(nums)-1:
                pos = self.bin_search(nums, target, index, len(nums)-1)
        return -1!=pos

    def find_rotation_point(self, nums: List[int], start, end):
        if end-start==1:
            if nums[end]<nums[start]:
                return end
            return 
        if end==start:
            if nums[start-1]>nums[start]:
                return start
            if nums[start+1]<nums[start]:
                return start+1
            return 0
        mid = (start+end)//2
        return self.find_rotation_point(nums, start, mid)+self.find_rotation_point(nums, mid, end)

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
        return self.bin_search(nums, target, start, mid)0
