from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = [i for j in mat for i in j] 
        if r*c!=len(arr):
            return mat
        shaped_matrix = [[arr[i] for i in range(x, x+c)] for x in range(0, len(arr), c)]
        return shaped_matrix 


if __name__ == "__main__":
    sol = Solution().matrixReshape
    assert sol(mat=[[1,2], [3,4]], r=1, c=4) == [[1,2,3,4]]
    assert sol(mat=[[1,2],[3,4]], r=2, c=4) == [[1,2], [3,4]]
    print("All tests passed successfully!")

