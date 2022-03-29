import math

class Solution:
    d = {1:False, 2:True, 3:False, 4:True, 5:False}
    ma = 5

    def divisorGame(self, n: int) -> bool:
        if n not in self.d:
            for i in range(self.ma+1, n+1):
                self.d[i] = False
                for k in range(1, int(math.sqrt(i))+1):
                    if i%k==0:
                        if self.d[i-k] == False:
                            self.d[i] = True   
                            break
            self.ma = n
        return self.d[n]

        
