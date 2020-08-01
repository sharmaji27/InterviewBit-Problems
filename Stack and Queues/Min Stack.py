'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor. 
'''
class MinStack:
    # @param x, an integer
    
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        cur_min = self.getMin()
        if cur_min==-1 or cur_min > x:
            cur_min = x
        self.stack.append([x,cur_min])

    # @return nothing
    def pop(self):
        try:
            self.stack.pop()
        except:
            pass
        
    # @return an integer
    def top(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1][0]
    
    # @return an integer
    def getMin(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1][1]
