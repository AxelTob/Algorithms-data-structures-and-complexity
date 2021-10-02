# n - nbr nodes
# m - number of edges in
# c - number of students to transfer
# p - nbr of routes in your plan
import copy
# import numpy as np

from collections import defaultdict


class Graph:

    def __init__(self, n):
        self.graph = [[0 for i in range(n)] for j in range(n)]
        self.N = n
        self.paths = []
        self.source = 0
        self.sink = n - 1

    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def bfs(self, path):
        visited = set()
        queue = [self.source]

        visited.add(self.source)
        while queue:
            u = queue.pop(0)



            for ind, cap in enumerate(self.graph[u]):
                if ind not in visited and cap is not 0:
                    visited.add(ind)
                    path[ind] = u
                    queue.append(ind)

        # we return true if we found sink
        return self.sink in visited

    def ford_fulkerson(self):

        path = [-1] * n
        #path = {}
        while self.bfs(path):
            # empty

            path_flow = float("Inf")
            s = self.sink

            # find the smallest capacity along the path

            while (s != self.source):
                path_flow = min(path_flow, self.graph[path[s]][s])
                s = path[s]
            self.paths.append([path, path_flow])
            # Add path flow to overall flow

            # Take away the capacity of the path

            # Take away the capacity of the path -- SÄG FÖRST
            v = self.sink
            while (v != self.source):
                u = path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] -= path_flow

                v = path[v]



    def GetMaxFlow(self):
        max_flow = 0
        for _, path_flow in self.paths:
            max_flow += path_flow
        return max_flow


# --- inputs ---
n, m, c, p = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for i in range(m)]
remove_order = [int(input()) for x in range(p)]

# --- Matrix -----
matrix = [[0 for i in range(n)] for j in range(n)]

G = Graph(n)


for i, edge in enumerate(edges):
    if i not in remove_order:
        u, v, w = edge
        G.addEdge(u, v, w)

# build graph, anropa med matrix. Fill graph with
graph = Graph(n)
graph.ford_fulkerson()
flow = G.GetMaxFlow()


for i, j in enumerate(remove_order[::-1]):

    # if flow is fine

    if flow >= c:
        print(str(len(remove_order) - i) + " " + str(flow))
        break
    u, v, w = edges[j]

    G.addEdge(u, v, w)
    G.ford_fulkerson()
    flow = G.GetMaxFlow()

