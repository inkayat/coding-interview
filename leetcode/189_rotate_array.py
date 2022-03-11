from typing import List
import math 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k%n==0:
            return
        k%=n
        q = 0
        while math.gcd(k, n) != 1:
            k-=1 
            q+=1
        temp = nums[k]
        nums[k] = nums[0]
        t = k
        for i in range(1, n):
            t = (t+k)%n
            prev = nums[t]
            nums[t] = temp
            temp = prev
        while q>0:
            last = nums[-1]
            for i in range(n-2, -1, -1):
                nums[i+1] = nums[i]
            nums[0] = last
            q-=1
        return 

if __name__ == "__main__":
    sol = Solution().rotate
    assert sol(nums=[1,2,3,4,5,6], k=4) == [3,4,5,6,1,2]
    assert sol(nums = [1,2,3,4,5,6], k = 3) == [4,5,6,1,2,3]
    assert sol(nums = [1,2,3,4,5,6,7], k = 4) == [4,5,6,7,1,2,3]
    assert sol(nums = [1,2,3,4,5,6,7], k = 3) == [5,6,7,1,2,3,4]
    assert sol(nums=[-1,-100,3,99], k=2) == [3,99,-1,-100]
    print("All tests passed successfully!")
