from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums)-1)

    def helper(self, arr, target, start, end):
        if end-start<=1:
            if arr[start] == target:
                return start
            elif arr[end] == target:
                return end 
            return -1
        mid = (start+end)//2 
        if arr[mid] > target:
            return self.helper(arr, target, start, mid)
        return self.helper(arr, target, mid, end)

if __name__ == "__main__":
    sol = Solution().search 
    assert sol(nums=[-1,0,3,5,9,12], target=9) == 4 
    assert sol(nums=[-1,0,3,5,9,12], target=2) == -1
    print("All tests passed successfully!")
