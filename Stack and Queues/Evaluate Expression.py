'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.



Input Format

The only argument given is character array A.
Output Format

Return the value of arithmetic expression formed using reverse Polish Notation.
For Example

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9
    
Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        value_stack = []
        operator_stack = []
        
        def evaluate(op,val1,val2):
            if op=='+': return val1+val2
            elif op=='-': return val2-val1
            elif op=='*': return val1*val2
            elif op=='/': return val2//val1
        
        
        for i in range(len(A)):
            if A[i].isdigit() or (A[i][0]=='-' and A[i]!='-'):
                value_stack.append(int(A[i]))
            
            elif A[i] in '+-*/':
                val1 = value_stack.pop()
                val2 = value_stack.pop()
                value_stack.append(evaluate(A[i],val1,val2))
        
        return(value_stack[-1])