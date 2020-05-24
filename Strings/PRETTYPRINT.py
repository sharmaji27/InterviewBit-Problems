'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        res = [[0]*((2*A)-1) for _ in range((2*A)-1)]
        step=0
        row=0
        for row in range(A):
            for i in range(A):
                if i<step:
                    res[row][i] = res[row-1][i]    
                else:
                    res[row][i] = A-step
            step+=1
        
        for row in range(A):
            res[row][A:2*A-1] = res[row][:A-1][::-1]
        
        x = A-2
        for row in range(A,2*A-1):
            res[row] = res[x]
            x-=1 
        
        return(res)