'''
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4 
so minimum numbers will be 2 
'''
class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        f = [1,1]
        while f[-1]<A:
        	f.append(f[-1]+f[-2])
        f = list(set(f))
        f.sort(reverse=True)
        c = 0
        for i in f:
        	if i<=A:
        		c+=1
        		A-=i
        	if A==0:break
        
        return(c)