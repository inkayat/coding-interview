class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        n = len(nums)
        while i>0 and (nums[i]<=nums[i-1]):
            i-=1
        if i==0:
            for i in range(n//2):
                nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
        else:
            if nums[-1]>nums[i-1]:
                k=n
            else:
                k=i+1
                while k<n and nums[i-1]<nums[k]:
                    k+=1
            nums[i-1],nums[k-1]=nums[k-1],nums[i-1]
            j=0
            while i+j<n-1-j:
                nums[i+j], nums[n-j-1]=nums[n-j-1],nums[i+j]
                j+=1
        return nums
            
