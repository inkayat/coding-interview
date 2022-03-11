from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))
        arr.sort(key=lambda x: [i for i in x], reverse=True)
        for i in range(1, len(arr)):
            j = i
            while j>0 and arr[j]+arr[j-1] > arr[j-1]+arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j-=1
        if arr[0] == "0":
            return arr[0]
        return ''.join(arr)

if __name__ == "__main__":
    assert Solution().largestNumber(nums=[10,2]) == "210"
    assert Solution().largestNumber(nums=[3,30,34,5,9]) == "9534330"
    print("All tests passed successfully!")

