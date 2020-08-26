class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, rect):
        def largestRectangleArea(A):
            stack = []
            maxi = 0
            i = 0
            while i<len(A):
                if len(stack)==0 or A[stack[-1]]<=A[i]:
                    stack.append(i)
                    i+=1
                else:
                    top = stack.pop()
                    if len(stack)==0:
                        ar = A[top]*(i)
                    else:
                        ar = A[top]*(i-stack[-1]-1)
                    maxi = max(maxi,ar)
        
            while len(stack)!=0:
                top = stack.pop()
                if len(stack)==0:
                    ar = A[top]*(i)
                else:
                    ar = A[top]*(i-stack[-1]-1)
                maxi = max(maxi,ar)
        
            return(maxi)
        
        m = largestRectangleArea(rect[0])
        rows = len(rect)
        cols = len(rect[0])
        
        for i in range(1,rows):
            for j in range(cols):
                if rect[i][j]==1:
                    rect[i][j] = rect[i-1][j]+1
            m = max(m,largestRectangleArea(rect[i]))
        
        return (m)