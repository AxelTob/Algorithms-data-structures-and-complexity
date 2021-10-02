import collections
# https://people.eecs.berkeley.edu/~vazirani/algorithms/chap5.pdf
# limited by sorting the edges O(E*logE)
# medium spanning tree - a subset of edges which connect all vertices in the graph with the minimal total edge cost of


# Kan göras snabbare med path compression, ref direkt till source för subgroup

parent = {}
rank = {}

# if node is in root it will recursively call till it finds source node - O(log*N)?
# Kan göras till O(1)
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

# Merge smaller components into the larger ones
#
def union(u, v):
    # determine which "group" the V belongs to
    u = find(u)
    v = find(v)

    if rank[u] > rank[v]:
        # point it to the larger group
        parent[v] = u
        rank[u] += 1
    else:
        parent[u] = v
        rank[v] += 1


def kruskal(nodes, edges):
    # for each node set it as root

    #O(V)
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    sum = 0
    # sort the edges by weight - so we pick them in increasing order - O(E logE)
    edges.sort(key=lambda x: x[2])

    # O(V logV) ?
    for edge in edges:
        u, v, weight = edge
        # print(parent)
        # check so they won't create a cycle
        if find(u) != find(v):
            sum += weight
            # add
            union(u, v)

            # T.append(edge)

    return sum


def main():
    N, M = (int(x) for x in input().split(" "))

    edges = []
    nodes = set()
    for _ in range(M):
        u, v, weight = [int(x) for x in input().split(" ")]
        nodes.add(u)
        nodes.add(v)
        edges.append([u, v, weight])

    T = kruskal(nodes, edges)

    print(T)


if __name__ == "__main__":
    main()
