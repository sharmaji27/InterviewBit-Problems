'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, n):
        l=[[1] , [1,1] , [1,2,1]]
        if n<0:
            return 
        elif n<3:
            return (l[n])
        else:
            n=n+1
            for i in range(4,n+1):
                a=[1]
                if i%2==0:
                    for i in range(i//2):
                        a.append(l[-1][i]+l[-1][i+1])
                    re = a+a[::-1][2:]
                else:
                    for i in range(i//2):
                        a.append(l[-1][i]+l[-1][i+1])
                    re = a+a[::-1][1:]
                l.append(re)
                
            return(l[-1])