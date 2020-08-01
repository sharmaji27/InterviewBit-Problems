'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        retlist = []
        if (A < 0) ^ (B < 0) and (A != 0):
			retlist.append('-')
        A = abs(A)
        B = abs(B)
        retlist.append(str(A//B))
        
        if A%B:
            retlist.append('.')
        hashmap = {}
        rem = A%B
        
        while rem and rem not in hashmap:
            hashmap[rem] = len(retlist)-1
            rem = 10*rem
            retlist.append(str(rem//B))
            rem = rem % B
            
        if rem :
            retlist.insert(hashmap[rem]+1, '(')
            retlist.append(')')
        
        return(''.join(retlist))