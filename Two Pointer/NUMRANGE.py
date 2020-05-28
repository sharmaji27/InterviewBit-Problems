'''
Given an array of non negative integers A, and a range (B, C),
find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
where 0 <= i <= j < size(A)

Example :

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3
as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]

 NOTE : The answer is guranteed to fit in a 32 bit signed integer.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        i = 0
        j = 0
        s = 0
        c = 0
        x = len(A)-1
        
        while i<=x:
            s += A[j]
            if s>=B and s<=C:
                c+=1
                j+=1
            elif s<B:
                j+=1
            elif s>C:
                i+=1
                j=i
                s=0
            if j==x+1:
                i+=1
                j=i
                s=0
        
        return(c)