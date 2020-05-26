'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)


'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        closest = A[0]+A[1]+A[2]
        A.sort()
        
        for i in range(len(A)-2):
            l = i+1
            r = len(A)-1
        
            while l<r:
                current = A[i]+A[l]+A[r]
                if abs(B - current) < abs(B - closest):
                        closest = current
        
                if current < B:
                    l+=1
                elif current > B:
                    r-=1
                else:
                    return(closest)
        return(closest)