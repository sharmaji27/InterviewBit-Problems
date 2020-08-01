'''
Given a string A, find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.

You need to return the length of longest palindromic subsequence in A.

NOTE:

Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.


Problem Constraints
1 <= |A| <= 1005



Input Format
First and only argument is an string A.



Output Format
Return a integer denoting the length of longest palindromic subsequence in A.



Example Input
Input 1:

 A = "bebeeed"


Example Output
Output 1:

 4


Example Explanation
Explanation 1:

 The longest common pallindromic subsequence is "eeee", which has a length of 4
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l = len(A)

        dp_matrix = [[0 for _ in range(l)] for _ in range(l)]
        
        for i in range(l):
        	dp_matrix[i][i]=1
        
        
        for i in range(l-1,-1,-1):
        	for j in range(i+1,l):
        		if A[i]==A[j]:
        			dp_matrix[i][j] = dp_matrix[i+1][j-1]+2
        		else:
        			dp_matrix[i][j] = max(dp_matrix[i+1][j],dp_matrix[i][j-1])
        
        return(dp_matrix[0][-1])