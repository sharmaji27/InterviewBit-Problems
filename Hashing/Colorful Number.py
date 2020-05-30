'''
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1
'''
class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
        s  = set()
        A = str(A)
        def multiplier(s):
            s = list(s)
            x = 1
            for y in s:
                x *= int(y)
            return x
        
        for i in range(len(A)):
            for j in range(i,len(A)):
                x = multiplier(A[i:j+1])
                if x in s:
                    return(0)
                else:
                    s.add(x)
        return(1)