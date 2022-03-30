from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
        else:
            digits[-1] = 0
            i = len(digits)-2
            while i>=0 and digits[i]+1==10:
                digits[i]=0
                i-=1
            if i==-1:
                digits = [1]+digits
            else:
                digits[i]+=1
        return digits
