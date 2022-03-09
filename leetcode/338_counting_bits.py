from typing import List 

class Solution:

    calculated = {0:0, 1:1, 2:1, 3:2, 4:1, 5:2}

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n+1):
            if i not in self.calculated:
                self.calculated[i] = self.calculated[i>>1] + self.calculated[1&i] 
            res.append(self.calculated[i])
        return res

if __name__ == "__main__":
    sol = Solution().countBits
    assert sol(n=2) == [0,1,1]
    assert sol(n=5) == [0,1,1,2,1,2]
    assert sol(n=20) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2]
    print("All tests passed successfully!")
