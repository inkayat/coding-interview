class Solution:
    
    calculated = {1:0, 2:1, 3:2, 4:4, 5:6, 6:9, 7:12, 8:18, 9:27, 10:36}

    def integerBreak(self, n: int) -> int:
        if n in self.calculated:
            return self.calculated[n]
        for i in range(11, n+1):
            self.calculated[i] = 0
            for j in range(1, i-1):
                self.calculated[i] = max(self.calculated[i], j*self.calculated[i-j])
        return self.calculated[n]


assert Solution().integerBreak(n=2) == 1 
assert Solution().integerBreak(n=10) == 36
print("All tests passed successfully!")
