'''
Given a binary tree A consisting of N nodes, return a 2-D array denoting the vertical order traversal of A.

Go through the example and image for more details.

NOTE:

If 2 or more Tree Nodes shares the same vertical level then the one with earlier occurence in the pre-order traversal of tree comes first in the output.
Row 1 of the output array will be the nodes on leftmost vertical line similarly last row of the output array will be the nodes on the rightmost vertical line.


Problem Constraints
0 <= N <= 104



Input Format
First and only argument is an pointer to root of the binary tree A.



Output Format
Return a 2D array denoting the vertical order traversal of A.



Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

           1
         /   \
        2     3
       / \
      4   5


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [4],
    [2],
    [1, 5],
    [3]
 ]


Example Explanation
Explanation 1:

 
 Nodes on Vertical Line 1: 2
 Nodes on Vertical Line 2: 3
 Nodes on Vertical Line 3: 6, 5
    As 6 and 5 are on the same vertical level but as 6 comes first in the pre-order traversal of the tree so we will output 6 before 5.
 Nodes on Vertical Line 4: 7
 Nodes on Vertical Line 5: 9
Explanation 2:

 Nodes on Vertical Line 1: 4
 Nodes on Vertical Line 2: 2
 Nodes on Vertical Line 3: 1, 5
 Nodes on Vertical Line 4: 3
'''
class Solution:
	def verticalOrderTraversal(self, A):
	    if A is None:return []
	    q=[(A,0)]
	    d={}
	    while q:
	        curr,x = q.pop(0)
	        d.setdefault(x,[]).append(curr.val)
	        if curr.left:q.append((curr.left,x-1))
	        if curr.right:q.append((curr.right,x+1))
	    return [d[x] for x in sorted(d.keys())]