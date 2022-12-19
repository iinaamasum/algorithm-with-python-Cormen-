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
        print("MST: ")
        print("Edge\tWeight")
        for u, v, w in A:
            print(f"{u} - {v}  :  {w}")
        print("-" * 15)
        print("MST sum: ", mst_sum)


if __name__ == "__main__":
    edges = int(input("Enter the number of edges: "))
    g = Graph(edges)
    for i in range(edges):
        u, v, w = map(int, input("Enter Edge and Weight: ").split(" "))
        g.addEdge(u, v, w)
    print("\nEntered graph: ")
    print("Edge\tWeight")
    for u, v, w in g.graph:
        print(f"{u} - {v}  :  {w}")
    print()
    g.krushkalMST()


""" 
input
3
0 1 10
1 2 5
0 2 20

9
5 1 4
5 4 7
1 4 1
4 3 5
4 2 8
1 2 2
2 3 3
3 6 8
2 6 7
"""

""" 
Enter the number of edges: 9
Enter Edge and Weight: 5 1 4
Enter Edge and Weight: 5 4 7
Enter Edge and Weight: 1 4 1
Enter Edge and Weight: 4 3 5
Enter Edge and Weight: 4 2 8
Enter Edge and Weight: 1 2 2 
Enter Edge and Weight: 2 3 3 
Enter Edge and Weight: 3 6 8
Enter Edge and Weight: 2 6 7

Entered graph: 
Edge    Weight
5 - 1  :  4
5 - 4  :  7
1 - 4  :  1
4 - 3  :  5
4 - 2  :  8
1 - 2  :  2
2 - 3  :  3
3 - 6  :  8
2 - 6  :  7

MST: 
Edge    Weight
1 - 4  :  1
1 - 2  :  2
2 - 3  :  3
5 - 1  :  4
2 - 6  :  7
---------------
MST sum:  17
"""
