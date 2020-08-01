'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
'''
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n=0
        for i in range(len(A)):
            n = 26*n + ord(A[i])-64
        return n