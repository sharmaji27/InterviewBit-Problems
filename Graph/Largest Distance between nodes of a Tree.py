'''
Given an arbitrary unweighted rooted tree which consists of N nodes.

The goal of the problem is to find largest distance between two nodes in a tree.

Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.



Problem Constraints
1 <= N <= 40000



Input Format
First and only argument is an integer array A of size N.



Output Format
Return a single integer denoting the largest distance between two nodes in a tree.



Example Input
Input 1:

 A = [-1, 0, 0, 0, 3]


Example Output
Output 1:

 3


Example Explanation
Explanation 1:

 node 0 is the root and the whole tree looks like this: 
          0
       /  |  \
      1   2   3
               \
                4

 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3.
'''
from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        graph = {}
        
        for i in range(len(A)):
            if A[i]==-1:root = i
            else:
                graph.setdefault(A[i],[]).append(i)
                graph.setdefault(i,[]).append(A[i])
        
        def bfs(root):
            visited = set()
            q = deque([(root,0)])
            while q:
                curr,level = q.popleft()
                if q==deque([]):
                    x,y =  curr,level
                if curr in graph:
                    for n in graph[curr]:
                        if n not in visited:
                            q.append((n,level+1))
                            visited.add(n)
                visited.add(curr)
            return x,y
        
        node1,cost1 = bfs(root)
        node2,cost2 = bfs(node1)
        return cost2