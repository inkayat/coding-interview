from typing import List 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.found = -1
        nums = [-1<<32]+nums+[-1<<32]
        self.search_peak(nums, 1, len(nums)-2)
        return self.found

    def search_peak(self, nums: List, start, end):
        if self.found != -1:
            return
        if nums[start-1] < nums[start] > nums[start+1]:
            self.found = start-1
            return
        elif nums[end-1] < nums[end] > nums[end+1]:
            self.found = end-1
            return
        if end-start<=1:
            return 
        mid = (start+end)//2
        self.search_peak(nums, start,  mid) 
        self.search_peak(nums, mid, end)
        

if __name__ == "__main__":
    sol = Solution().findPeakElement 
    assert(sol(nums = [1,2,3,1])) in [2] 
    assert(sol(nums = [1,2,1,3,5,6,4])) in [1, 5] 
    assert (sol(nums=[1,2,1,5,6,7,8,9])) in [1, 7]
    assert(sol(nums = [5])) in [0]
    print("All tests passed successfully!")
