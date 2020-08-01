'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, s, numRows):
        if numRows<=1:
            return s
        i=0
        res = ['']*numRows
        step = 0
        row=0
        
        while i<len(s):
            if row==numRows-1:
                step = 1
            if row==0:
                step = 0
        
            if step==0:
                res[row]+=(s[i])
                row+=1
            elif step==1:
                res[row]+=(s[i])
                row-=1
            i+=1
        return(''.join(res))