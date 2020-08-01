'''
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, s):
        s = s.strip()
        sign = 1
        num = '0'
        if len(s)==0:
            return 0
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        if len(s)==0:
            return 0
        for i in range(len(s)):
            if s[i].isdigit():
                num+=s[i]
            else:
                break
        
        if sign==-1:
            return(max(-2**31,sign*int(num)))
        else:
            return(min((2**31)-1,sign*int(num)))