from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.search_row(matrix, target, 0, len(matrix)-1)
        if matrix[row][0] >target or matrix[row][-1]<target:
            return False 
        col = self.search_col(matrix, target, row, 0, len(matrix[0])-1)
        if col !=- 1:
            return True 
        return False


    def search_row(self, mat, target, start, end):
        if end-start<=1:
            if mat[end][0] <= target:
                return end 
            return start 
        mid = (start+end)//2 
        if mat[mid][0]>target:
            return self.search_row(mat, target, start, mid)
        return self.search_row(mat, target, mid, end) 

    def search_col(self, mat, target, row, start, end): 
        if end-start<=1:
            if mat[row][start] == target:
                return start 
            elif mat[row][end] == target:
                return end
            return -1
        mid = (start+end)//2
        if mat[row][mid] > target:
            return self.search_col(mat, target, row, start, mid) 
        return self.search_col(mat, target, row, mid, end)

if __name__ == "__main__":
    sol = Solution().searchMatrix 
    assert sol(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) == True 
    assert sol(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13) == False
    assert sol(matrix = [[1,3,5]], target = 3) == True
    assert sol(matrix = [[1,3,5]], target=5) == True
    print("All tests passed successfully!")
    
