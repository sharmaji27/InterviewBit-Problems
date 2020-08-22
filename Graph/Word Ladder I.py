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