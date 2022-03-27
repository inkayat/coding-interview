from itertools import combinations
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = [i for i in d[digits[0]]]
        for i in range(1, len(digits)):
            temp = []
            for k in res:
                for j in d[digits[i]]:
                    temp.append(k+j)
            res = temp
        return res
            
