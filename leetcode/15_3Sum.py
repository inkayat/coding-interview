from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums)<3:
            return []
        res = []
        i = 0
        prev = -1
        while i < len(nums)-2:
            if (prev != -1 and nums[prev] == nums[i]):
                i+=1
                continue
            x, y, z = i, i+1, len(nums)-1
            prev = x
            cur_sum = nums[i]+nums[i+1]+nums[-1]
            i+=1
            while y<z:
                if cur_sum == 0:
                    res.append([nums[x], nums[y], nums[z]])
                    while z>0 and nums[z] == nums[z-1]:
                        z-=1
                    z-=1
                    y+=1
                elif cur_sum>0:
                    z-=1 
                else:
                    y+=1
                cur_sum=nums[x]+nums[y]+nums[z]
        return res

if __name__ == "__main__":
    sol = Solution().threeSum
    assert sol(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert sol(nums=[]) == []
    assert sol(nums=[-10, 1, 2, -2, -3, 3, 4, 5, -7, 5, 15, -20]) == [[-20, 5, 15], [-10, 5, 5], [-7, 2, 5], [-7, 3, 4], [-3, -2, 5], [-3, 1, 2]]
    assert sol(nums=[0, 0, 0]) == [[0, 0, 0]]
    assert sol(nums=[-2,0,0,2,2]) == [[-2,0,2]]
    print("all test passed successfully!")

