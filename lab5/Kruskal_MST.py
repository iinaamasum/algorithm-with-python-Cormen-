class Graph:
    def __init__(self, vertex) -> None:
        self.V = vertex
        self.graph = []
        self.parent = []
        self.rank = []

    def addEdge(self, u, v, w) -> None:
        self.graph.append([u, v, w])

    def disjointSetMake(self):
        for i in range(self.V):
            self.parent.append(i)
            self.rank.append(0)

    def disjointSetFind(self, val):
        if self.parent[val] == val:
            return val
        self.parent[val] = self.disjointSetFind(self.parent[val])
        return self.parent[val]

    def disjointSetUnion(self, u, v):
        ul_parent_u = self.disjointSetFind(u)
        ul_parent_v = self.disjointSetFind(v)

        if self.rank[ul_parent_u] < self.rank[ul_parent_v]:
            self.parent[ul_parent_u] = ul_parent_v
        elif self.rank[ul_parent_u] > self.rank[ul_parent_v]:
            self.parent[ul_parent_v] = ul_parent_u
        else:
            self.parent[ul_parent_u] = ul_parent_v
            self.rank[ul_parent_u] += 1

    def krushkalMST(self):
        A = []
        mst_sum = 0
        # disjoint set making
        self.disjointSetMake()

        # sorting the graph according to weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for u, v, w in self.graph:
            if self.disjointSetFind(u) != self.disjointSetFind(v):
                A.append([u, v, w])
                mst_sum += w
                self.disjointSetUnion(u, v)
        print("MST sum: ", mst_sum)
        print("MST: ")
        print("Edge\tWeight")
        for u, v, w in A:
            print(f"{u} - {v} : {w}")


if __name__ == "__main__":
    edges = int(input("Enter the number of edges: "))
    g = Graph(edges)
    for i in range(edges):
        u, v, w = map(int, input("Enter Edge and Weight: ").split(" "))
        g.addEdge(u, v, w)
    print("\nEntered graph: ")
    print("Edge\tWeight")
    for u, v, w in g.graph:
        print(f"{u} - {v} : {w}")
    print()
    g.krushkalMST()


""" 
input
3
0 1 10
1 2 5
0 2 20
"""
