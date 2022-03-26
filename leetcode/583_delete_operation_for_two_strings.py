from collections import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = defaultdict(lambda:defaultdict(lambda:-1))
        return self.helper(word1, word2, 0, 0)
    
    def helper(self, word1, word2, x, y):
        if x == len(word1):
            return len(word2)-y
        elif y == len(word2):
            return len(word1)-x
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        if word1[x] == word2[y]:
            self.dp[x][y] =self.helper(word1, word2, x+1,y+1)
        else:
            self.dp[x][y] = 1+min(self.helper(word1, word2, x+1, y), self.helper(word1,word2,x,y+1))
        return self.dp[x][y]
