'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.



A sudoku puzzle,



and its solution numbers marked in red.

Example :

For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]

'''
class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    board[i][j] = int(board[i][j])
                else:
                    board[i][j] = 0
                    
        def return_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]==0:
                        return(i,j)
            return None
        
        def check(board,num,pos):
            row,col = pos
        
            # checking row
            for i in range(9):
                if board[row][i]==num and i!=col:
                    return False
        
            # checking col
            for i in range(9):
                if board[i][col]==num and i!=row:
                    return False
        
            # checking for sub-grid
            box_x = row//3
            box_y = col//3
        
            for i in range(box_x*3,box_x*3+3):
                for j in range(box_y*3,box_y*3+3):
                    if board[i][j]==num and (i,j)!=pos:
                        return False
            return True
        
        def solve(board):
            vacant = return_empty(board)
            if vacant is None:return True #means all cella are filled now and we have completed the sudoku
            row,col = vacant
            for i in range(1,10):
                if check(board,i,vacant):
                    board[row][col] = i
                    if solve(board):
                        return True
                    board[row][col] = 0
            return False
        
        solve(board)

        for i in range(9):
            l = ''
            for j in range(9):
                l+=str(board[i][j])
            board[i] = l
        
        return board