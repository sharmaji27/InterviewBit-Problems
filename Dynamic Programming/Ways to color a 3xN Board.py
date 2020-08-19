'''
Given a 3 x A board, find the number of ways to color it using at most 4 colors such that no 2 adjacent boxes have same color.

Diagonal neighbors are not treated as adjacent boxes.

Return the ways modulo 109 + 7 as the answer grows quickly.

Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return an integer representing the number of ways to color the board.
Constraints:

1 <= A < 100000
Examples:

Input 1:
    A = 1

Output 1:
    36

Input 2:
    A = 2

Output 2:
    588
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        color2 = 12
        color3 = 24
        temp = 0
        
        for i in range(1,A):
            temp = color3
            color3 = (10*color2 + 11*color3)%1000000007
            color2 = (7*color2 + 5*temp)%1000000007
        
        return (color3+color2)%1000000007
            