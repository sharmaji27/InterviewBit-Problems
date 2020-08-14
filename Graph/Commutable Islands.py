'''
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Input Format:

The first argument contains an integer, A, representing the number of islands.
The second argument contains an 2-d integer matrix, B, of size M x 3:
    => Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].
Output Format:

Return an integer representing the minimal cost required.
Constraints:

1 <= A, M <= 6e4
1 <= B[i][0], B[i][1] <= A
1 <= B[i][2] <= 1e3
Examples:

Input 1:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 4]
            [1, 4, 3]
            [4, 3, 2]
            [1, 3, 10]  ]

Output 1:
    6

Explanation 1:
    We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.

Input 2:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 2]
            [3, 4, 4]
            [1, 4, 3]   ]

Output 2:
    6

Explanation 2:
    We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.

'''
from heapq import heappush, heappop


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_list = self.create_adj_list(A, B)

        start_node = 1  ## doesn't matter actually, because all nodes should be connected
                        ## so 1 must also be connected
        return self.total_cost_using_prim(adj_list, start_node)

    def create_adj_list(self, nodes_num, bridges):
        adj_list = [[] for _ in range(nodes_num + 1)]

        for source, dest, cost in bridges:
            adj_list[source] += [(dest, cost)]
            adj_list[dest] += [(source, cost)]

        return adj_list

    def total_cost_using_prim(self, adj_list, start_node):
        visited = set()
        pq = [(0, start_node)]
        total_cost = 0

        while len(pq) > 0:
            cost, cur_node = heappop(pq)

            if cur_node in visited: continue

            total_cost += cost

            for neighbor, neighbor_cost in adj_list[cur_node]:
                heappush(pq, (neighbor_cost, neighbor))

            visited.add(cur_node)

        return total_cost