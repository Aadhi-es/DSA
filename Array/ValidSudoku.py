class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Col checker
        for i in range(9):
            nums=set() # making a new set for each row and appending is not repeated
            for j in range(9):
                if board[j][i] in nums:
                    return False
                elif board[j][i] =='.':
                    continue
                else:
                    nums.add(board[j][i])
         #ROw checker
       
            num=set() # making a new set for each row and appending is not repeated
            for j in range(9):
                if board[i][j] in num:
                    return False
                elif board[i][j] =='.':
                    continue
                else:
                    num.add(board[i][j])

        #box checker
        boxstart=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)
        ]
        for row,col in boxstart: 
            # loop for each of the 9boxes
            nums=set()
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j] in nums:
                        return False
                    elif board[i][j]=='.':
                        continue
                    else:
                        nums.add(board[i][j])
        
        return True 


        


        