import string

class Solution:
    def convertToTitle(self, c: int) -> str:
        arr = string.ascii_uppercase
        res = ""
        while c>0:
            n = c%26
            c=int((c-0.001)//26)
            res = arr[n-1]+res
      
        return res
