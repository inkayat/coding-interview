class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


if __name__ == "__main__":
    sol = Solution().findMedianSortedArrays 
    assert sol(nums1=[1,3], nums2=[2]) == 2.0
    assert sol(nums1=[1,2], nums2=[3,4]) == 2.5
    assert (sol(nums1=[3,5,8,10], nums2=[1,2,4,6,9,12])) == 5.5
    print("All tests passed successfully!")
