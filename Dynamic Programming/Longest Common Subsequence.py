'''
Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints
1 <= |A|, |B| <= 1005



Input Format
First argument is an string A.

Second argument is an string B.



Output Format
Return the length of such longest common subsequence between string A and string B.



Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"


Example Output
Output 1:

 5


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        a = len(A)
        b = len(B)
        
        dp_matrix = [[0 for _ in range(a+1)] for _ in range(b+1)]
        
        for i in range(1,a+1):
        	for j in range(1,b+1):
        		if A[i-1]==B[j-1]:
        			dp_matrix[i][j] += dp_matrix[i-1][j-1]+1
        		else:
        			dp_matrix[i][j] = max(dp_matrix[i-1][j],dp_matrix[i][j-1])
        
        return(dp_matrix[-1][-1])