from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y, z = m-1, n-1, m+n-1
        while y>=0 and x>=0 and z>=0:
            if nums1[x]>nums2[y]:
                nums1[z] = nums1[x]
                x-=1
                z-=1 
            else:
                nums1[z] = nums2[y] 
                y-=1 
                z-=1
        while y>=0:
            nums1[z] = nums2[y] 
            y-=1 
            z-=1
        return nums1

        
if __name__ == "__main__":
    sol = Solution().merge 
    assert sol(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
    assert sol(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
    assert sol(nums1 = [0], m = 0, nums2 = [1], n = 1) == [1]
    assert sol(nums1 = [1,2,7,0,0,0], m=3, nums2 =[2,5,6], n=3) == [1,2,2,5,6,7]
    assert sol(nums1= [3,5,7,9,0,0,0,0,0], m=4, nums2=[1,2,4,6,8], n=5) == [1,2,3,4,5,6,7,8,9]
    print("All tests passed successfully!")
