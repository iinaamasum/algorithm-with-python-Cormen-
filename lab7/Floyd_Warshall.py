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


if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    for i in range(vertices):
        u, v, w = map(int, input("Enter the Edge and weight: ").split(" "))
        g.addEdge(u, v, w)
    # print(g.graph)
    g.FloydWarshall()
    print("\nAll pair shortest path: ")
    for i in range(vertices):
        if i == 0:
            print("\t\t", end="")
            continue
        print(i, end="\t\t")
    print()
    print("-" * 120)
    for i in range(vertices):
        print(i, end=" | ")
        for j in range(vertices):
            if g.graph[i][j] == maxsize:
                print("infinity", end="\t")
            else:
                print(g.graph[i][j], end="\t\t")
        print()
    print()

""" 
input
3
0 1 5
1 2 10
0 2 20

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
