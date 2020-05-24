'''
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more
details about roman numerals at Roman Numeric System



Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
'''
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, num):
        d= {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        s=0
        curr=0
        prev=0
        
        for i in num[::-1]:
            curr = d[i]
            if curr>=prev:
                s+=curr
            else:
                s-=curr
            prev=curr
            
        return(s)