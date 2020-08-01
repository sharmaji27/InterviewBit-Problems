'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java
'''
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, n):
        c = 0
        while n>=0:
            if n==0:
                return c
            c = c + (n%2)
            n//=2