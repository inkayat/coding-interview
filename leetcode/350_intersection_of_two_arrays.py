from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1, n2 = 0, 0
        result = []
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]<nums2[n2]:
                n1+=1
            elif nums2[n2]<nums1[n1]:
                n2+=1
            else:
                result.append(nums1[n1])
                n1+=1
                n2+=1
        return result


if __name__ == "__main__":
    sol = Solution().intersect 
    assert sol(nums1=[1,2,2,1], nums2=[2,2]) == [2,2] 
    assert sol(nums1=[4,9,5], nums2=[9,4,9,8,4]) == [4,9] 
    print("All tests are passed successfully!")
