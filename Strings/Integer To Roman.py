'''
Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

 Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations. 


Input Format

The only argument given is integer A.
Output Format

Return a string denoting roman numeral version of A.
Constraints

1 <= A <= 3999
For Example

Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"
'''
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX','X']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']
        M = ['','M','MM','MMM']
        
        return(M[A//1000] + C[(A%1000)//100] + X[(A%100)//10] + I[A%10])