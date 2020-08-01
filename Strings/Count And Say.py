'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A==1:
            return('1')
        else:
            prev_res = '1'
            for _ in range(2,A+1):
                s=''
                c=0
                ele = prev_res[0]
                for j in str(prev_res):
                    if j==ele:
                        c+=1
                    else:
                        s = s+str(c)+str(ele)
                        c=1
                        ele=j
                s = s+str(c)+j
                prev_res = s
        
            return(s)