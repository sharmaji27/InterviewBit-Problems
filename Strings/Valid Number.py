'''
Validate if a given string is numeric.

Examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Clarify the question using “See Expected Output”

Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem
'''
class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        n = len(A)
        if n == 0:
            return 0
        if A[0] == '+' or A[0] == '-':
            A = A[1:]
            n = n - 1
            if n == 0:
                return 0
        i = 0
        dotEncountered = False
        eEncountered = False
        while i < n:
            if A[i] >= '0' and A[i] <= '9':
                i += 1
                continue
            if A[i] == '.':
                if dotEncountered:
                    return 0
                dotEncountered = True
                i += 1
                if i >= n:
                	return 0
                elif A[i] == 'e':
                	return 0
            elif A[i] == 'e':
                if eEncountered:
                    return 0
                eEncountered = True
                dotEncountered = True
                i += 1
                if i < n and (A[i] == '-' or A[i] == '+'):
                	i += 1
            else:
            	return 0
        return 1
        