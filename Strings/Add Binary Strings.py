'''
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, a, b):
        m = len(a)-1
        n = len(b)-1
        carry = 0
        
        res = ''
        
        while m>=0 or n>=0 or carry!=0:
            if m>=0:
                carry+=int(a[m])
                m-=1
            if n>=0:
                carry+=int(b[n])
                n-=1
            res = str(carry%2) + res
            carry = carry//2
        
        return(res)