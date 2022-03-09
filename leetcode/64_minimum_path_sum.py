class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp = {}
        return self.helper(grid, 0, 0)
    
    def helper(self, arr, x, y):
        if x == len(arr) or y == len(arr[0]):
            return float('inf')
        if x == len(arr)-1 and y == len(arr[0])-1:
            return arr[x][y]
        if (x, y) in self.dp:
            return self.dp[(x,y)]
        self.dp[(x,y)]=arr[x][y]+min(self.helper(arr, x+1, y), self.helper(arr, x, y+1))
        return self.dp[(x,y)]
