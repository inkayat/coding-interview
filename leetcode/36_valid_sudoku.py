from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = {'row':{i:{} for i in range(9)}, 'col':{i:{} for i in range(9)}, 'sub':{i:{} for i in range(9)}}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isdigit():
                    if val in table['row'][i] or val in table['col'][j]:
                        return False
                    box = 0
                    if i<3:
                        if j<3:
                            box = 0
                        elif j<6:
                            box = 1
                        else:
                            box = 2
                    elif i<6:
                        if j<3:
                           box = 3
                        elif j<6:
                            box = 4
                        else:
                            box = 5
                    else:
                        if j<3:
                            box = 6
                        elif j<6:
                            box = 7
                        else:
                            box = 8
                    if val in table['sub'][box]:
                        return False
                    table['sub'][box][val] = 1
                    table['row'][i][val] = 1
                    table['col'][j][val] = 1
         
        return True 
