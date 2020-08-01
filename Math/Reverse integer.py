'''
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integerv
'''
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        s=1
        if A<0:
            s=-1
        A=abs(A)
        rev=0
        while A:
            rev = rev*10 + A%10
            A/=10
        if s*rev<2147483647 and s*rev>-2147483648:
            return s*rev
        else:
            return 0