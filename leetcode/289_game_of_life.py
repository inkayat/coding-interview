class Solution:
    
    def valid_points(self, x: int, y: int, m: int, n: int, board: List[List[int]]) -> List[set]:
        neighbors = [(0,-1),(-1,0), (0,1), (1,0), (-1,-1),(1,1),(1,-1),(-1,1)]
        return [(board[x+i][y+j]-2)%2 if (0<=x+i<m) and (0<=y+j<n) else 0 for i, j in neighbors]
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                arr = self.valid_points(i, j, m, n, board)
                one_zero = sum(arr)
                if one_zero == 3 and board[i][j] == 0:
                    board[i][j] = 2
                elif (one_zeo > 3 or one_zero<2) and board[i][j]==1:
                    board[i][j] = 3
            if i>0:
                for k in range(n):
                    if board[i-1][k]>1:
                        board[i-1][k] = (board[i-1][k]-1)%2
        for i in range(n):
            if board[m-1][i]>1:
                board[m-1][i] = (board[m-1][i]-1)%2
