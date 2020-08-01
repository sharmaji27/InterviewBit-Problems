'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, n):
        r=''
        while n>0:
            rem = n%26
            if rem==0:
                r +='Z'
                n=(n//26)-1
            else:
                r += chr(rem-1+ord('A'))
                n=n//26
        return(r[::-1])