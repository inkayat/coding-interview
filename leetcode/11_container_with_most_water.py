from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        while i!=j:
            if height[i]<height[j]:
                res = max(res, (j-i)*height[i])
                i+=1 
            else:
                res = max(res, (j-i)*height[j])
                j-=1 
        return res

            

assert Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]) == 49 
assert Solution().maxArea(height=[1,1]) == 1
