'''
Problem Description

Given a Binary Tree A consisting of N nodes.

You need to find all the cousins of node B.

NOTE:

Siblings should not be considered as cousins.
Try to do it in single traversal.
You can assume that Node B is there in the tree A.
Order doesn't matter in the output.


Problem Constraints
1 <= N <= 105

1 <= B <= N

Input Format
First Argument represents the root of binary tree A.

Second Argument is an integer B denoting the node number.

Output Format
Return an integer array denoting the cousins of node B.

NOTE: Order doesn't matter.

Example Input
Input 1:

 A =

           1
         /   \
        2     3
       / \   / \
      4   5 6   7 


B = 5

Input 2:

 A = 
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


B = 1


Example Output
Output 1:

 [6, 7]
Output 2:

 []


Example Explanation
Explanation 1:

 Cousins of Node 5 are Node 6 and 7 so we will return [6, 7]
 Remember Node 4 is sibling of Node 5 and do not need to return this.
Explanation 2:

Since Node 1 is the root so it doesn't have any cousin so we will return an empty array.

Seen this question in a real interview beforeYesNo
Share this    
NotesAll Notes

'''
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        q = [A]
        res = []
        found = False
        sz=0
        if A.val==B:
            return []
        
        while len(q)!=0 and not found:
            sz = len(q)
            while sz:
                c = q.pop(0)
                if ((c.left and c.left.val==B) or (c.right and c.right.val==B)):
                    found=True
                else:
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
                sz-=1
        for i in q:
            res.append(i.val)

        return res