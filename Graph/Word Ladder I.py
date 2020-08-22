'''
Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.
Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3
Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
'''
class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        graph = {}
        transformations = {}
        
        transform = lambda w: [(w[0:i]+'*'+w[i+1:]) for i in range (n)]
        
        for word in [A,B]:
        	transformations[word] = transform(word)
        	for w in transformations[word]:
        		if w not in graph:
        			graph[w]=[]
        		graph[w].append(word)
        
        for word in C:
        	transformations[word] = transform(word)
        	for w in transformations[word]:
        		if w not in graph:
        			graph[w]=[]
        		graph[w].append(word)
        
        
        visited = set()
        q = [(A,1)]
        
        while q:
        	curr,depth = q.pop(0)
        	if curr==B:
        		return (depth)
        	if curr in visited:continue
        	visited.add(curr)
        	for x in transformations[curr]:
        		for y in graph[x]:
        			if y not in visited:
        				q.append((y,depth+1))
        return 0