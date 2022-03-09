from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        for i in range(n-1):
            for j in range(1+i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix

if __name__ == "__main__":
    sol = Solution().rotate 
    assert sol([]) == []
    assert sol(matrix = [[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    assert sol(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print("All tests passed successfully!")
