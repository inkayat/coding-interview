class Solution:
    def generateMatrix(self, n: int):
        order = "right"
        i,j,k = 0,0,1
        arr = [[0 for _ in range(n)] for _ in range(n)]
        while k < n**2+1:
            if order == "right":
                while j<n and arr[i][j] == 0:
                    arr[i][j] = k 
                    k+=1
                    j+=1 
                j-=1 
                i+=1 
                order = "down" 
            elif order == "down":
                while i<n and arr[i][j] == 0:
                    arr[i][j] = k 
                    k+=1 
                    i+=1 
                i-=1 
                j-=1 
                order = "left" 
            elif order == "left":
                while j>-1 and arr[i][j] == 0:
                    arr[i][j] = k 
                    k+=1 
                    j-=1 
                j+=1 
                i-=1 
                order = "up" 
            else:
                while i>-1 and arr[i][j] == 0:
                    arr[i][j] = k 
                    k+=1 
                    i-=1 
                i+=1 
                j+=1
                order = "right"
        return arr

assert Solution().generateMatrix(n=3) == [[1,2,3],[8,9,4],[7,6,5]]
assert Solution().generateMatrix(n=1) == [[1]]
assert Solution().generateMatrix(n=4) == [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
assert Solution().generateMatrix(n=5) == [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
print("All test cases are passed successfully!")

