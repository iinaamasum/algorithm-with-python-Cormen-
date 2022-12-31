from sys import maxsize


class Graph:
    def __init__(self, vertex) -> None:
        self.V = vertex
        self.graph = [[maxsize for i in range(self.V)] for j in range(self.V)]

        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    self.graph[i][j] = 0

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    def FloydWarshall(self):
        for i in range(self.V):
            for j in range(self.V):
                for k in range(self.V):
                    self.graph[i][j] = min(
                        self.graph[i][j], self.graph[i][k] + self.graph[k][j]
                    )

    def printFloydWarshall(self):
        print("\nAll pair shortest path: ")
        print("    ", end="")
        for i in range(self.V):
            if i == 0:
                print("0\t\t", end="")
                continue
            print(i, end="\t\t")
        print()
        print("-" * 120)
        for i in range(self.V):
            print(i, end=" | ")
            for j in range(self.V):
                if g.graph[i][j] == maxsize:
                    print("infinity", end="\t")
                else:
                    print(g.graph[i][j], end="\t\t")
            print()
        print()


if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    for i in range(edges):
        u, v, w = map(int, input("Enter the Edge and weight: ").split(" "))
        g.addEdge(u, v, w)
    # print(g.graph)
    g.FloydWarshall()
    g.printFloydWarshall()


""" 
input
3
4
0 1 5
1 2 10
0 2 20
2 0 5

8
8
0 1 5
1 2 6
2 5 2
2 3 5
4 1 7
3 5 20
0 6 10
1 5 7
"""

""" 
Enter the number of vertices: 3
Enter the number of edges: 4
Enter the Edge and weight: 0 1 5
Enter the Edge and weight: 1 2 10
Enter the Edge and weight: 0 2 20
Enter the Edge and weight: 2 0 5

All pair shortest path: 
    0           1               2
------------------------------------
0 | 0           5               15
1 | 15          0               10
2 | 5           10              0
"""
