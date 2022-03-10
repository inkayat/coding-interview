import math
from typing import List

class Solution:
    
    triangle = [[math.comb(i, j) for j in range(0, i+1)] for i in range(30+1)]

    def generate(self, numRows: int) -> List[List[int]]:
        return self.triangle[:numRows]

if __name__ == "__main__":
    sol = Solution().generate 
    assert sol(numRows=5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert sol(numRows=1) == [[1]]
    print("All tests passed successfully!")
