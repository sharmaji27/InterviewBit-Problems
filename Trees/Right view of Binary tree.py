'''
Problem Description

Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 105

0 <= node values <= 109



Input Format
First and only argument is an pointer to the root of binary tree A.



Output Format
Return an integer array denoting the right view of the binary tree A.



Example Input
Input 1:

        1
      /   \
     2    3
    / \  / \
   4   5 6  7
  /
 8 
Input 2:

    1
   /  \
  2    3
   \
    4
     \
      5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]
'''
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A==None:
            return None
        q = [A]
        ans = []
        while q:
            temp = []
            row = []
            while q:
                curr = q.pop(0)
                row.append(curr.val)
                if curr.left:temp.append(curr.left)
                if curr.right:temp.append(curr.right)
            q=temp
            ans.append(row[-1])
        return ans