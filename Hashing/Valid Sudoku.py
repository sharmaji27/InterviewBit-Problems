'''
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        d = {}

        for i in range(9):
            for j in range(9):
                if A[i][j]!='.':
                    if ('{} in row {}'.format(A[i][j],i)) in d or ('{} in column {}'.format(A[i][j],j)) in d or ('{} in cell {}'.format(A[i][j],str(i//3) + str(j//3))) in d:
                        return(0)
                        
                    else:
                        d['{} in row {}'.format(A[i][j],i)] = 1
                        d['{} in column {}'.format(A[i][j],j)] = 1      
                        d['{} in cell {}'.format(A[i][j],str(i//3) + str(j//3))] = 1
        return(1)