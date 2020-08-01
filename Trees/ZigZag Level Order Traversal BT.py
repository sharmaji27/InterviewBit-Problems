'''
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        if root==None:
            return []
        q = []
        q.append(root)
        level = 1
        ans = []
        
        while len(q)!=0:
            tempq = []
            data = []
            while len(q)!=0:
                data.append(q[0].val)
                if q[0].left!=None:tempq.append(q[0].left)
                if q[0].right!=None:tempq.append(q[0].right)
                q.pop(0)
            if level%2==0:
                ans.append(data[::-1])
            else:
                ans.append(data)
            q = tempq
            level+=1
        return ans