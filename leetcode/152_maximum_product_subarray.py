### The fastest solution for maximum product sub array

from typing import List
from functools import reduce

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.res = -(1<<31)
        ret = self.helper(nums, 0)
        return self.res

    def helper(self, nums, x):
        if x == len(nums):
            return 0 
        elif x==len(nums)-1 or nums[x+1]==0:
            self.res = max(self.res, nums[x]) 
            return self.helper(nums, x+1) 
        if nums[x] == 0:
            self.res = max(self.res, 0)
            return self.helper(nums, x+1)
        prod = []
        neg = []
        temp = 1 
        i = x
        while i < len(nums):
            if nums[i] == 0:
                break 
            elif nums[i]<0:
                prod.append(temp) 
                neg.append(nums[i])
                temp=1
            else:
                temp*=nums[i]
            i+=1
        prod.append(temp)
        if len(neg)%2==0:
            self.res = max(self.res, reduce(lambda x,y:x*y, prod, 1)*reduce(lambda x,y:x*y, neg,1))
        else:
            self.res = max(self.res, max(reduce(lambda x,y:x*y, prod[1:],1)*reduce(lambda x,y:x*y, neg[1:],1) \
                    ,reduce(lambda x,y:x*y, prod[:-1],1)*reduce(lambda x,y:x*y, neg[:-1],1)))
        return self.helper(nums,i)



assert Solution().maxProduct(nums=[-2,0,-1]) == 0
assert Solution().maxProduct(nums=[-2]) == -2
assert Solution().maxProduct(nums=[0,2]) == 2
assert Solution().maxProduct(nums=[-1,-2,-3,-4]) == 24
assert Solution().maxProduct(nums=[-1,-2]) == 2
assert Solution().maxProduct(nums=[-1,-2,-3]) == 6
assert Solution().maxProduct(nums=[2,-3,-2,-8]) == 16 
assert Solution().maxProduct(nums=[2,-3,-2,-4]) ==  12
assert Solution().maxProduct(nums=[-2]) == -2
assert Solution().maxProduct(nums=[-4,-3,-2,-1,5,-2,-6,-8]) == 2880
assert Solution().maxProduct(nums=[2,3,-2,4]) == 6 
assert Solution().maxProduct(nums=[-3, 2,3, 5, -2,4, 6, -4, 3,7]) == 120960
assert Solution().maxProduct(nums=[-2,0,-1]) == 0 
print("All tests passed successfully!")
