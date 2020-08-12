'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
The same letter cell may be used more than once.

Example :

Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0
Note that 1 corresponds to true, and 0 corresponds to false.
'''
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, board, word):
        for i in range(len(board)):
        	board[i] = list(board[i])
        
        rows = len(board)
        cols = len(board[0])
        
        
        where = set()
        where2 = []
        dire = [(-1,0),(0,-1),(0,1),(1,0)]
        
        def add_neighbours(i,j,where,where2):
        	for x,y in dire:
        		if 0<=i+x<rows and 0<=y+j<cols:
        			where.add((i+x,y+j))
        			where2.append(board[i+x][y+j])
        
        
        for i in range(rows):
        	for j in range(cols):
        		if word[0] and board[i][j]==word[0]:
        			add_neighbours(i,j,where,where2)
        
        if len(where)==0:
            return 0
        
        for cw in range(1,len(word)):
        	temp  = where
        	temp2 = where2
        	if word[cw] in temp2:
        		where = set()
        		where2 = []
        		for wx,wy in temp:
        			if board[wx][wy]==word[cw]:
        				add_neighbours(wx,wy,where,where2)
        	else:
        		return 0	
        
        return 1