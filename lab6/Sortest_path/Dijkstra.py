import sys
from heapq import heappush, heappop


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, u: int, v: int, w: int) -> None:
        if u in self.graph:
            self.graph[u]["adjacent"].append([v, w])
        else:
            self.graph[u] = {}
            self.graph[u]["property"] = {"parent": None, "distance": sys.maxsize}
            self.graph[u]["adjacent"] = [[v, w]]

        if v not in self.graph:
            self.graph[v] = {}
            self.graph[v]["property"] = {"parent": None, "distance": sys.maxsize}
            self.graph[v]["adjacent"] = []

    def dijkstra(self, s: int) -> None:
        self.graph[s]["property"]["distance"] = 0

        # taking result set
        S = []
        Q = []

        for key in self.graph.keys():
            heappush(Q, key)

        while Q:
            u = heappop(Q)
            S.append(u)

            for key, val in self.graph.items():
                for edge in val["adjacent"]:
                    self.relax(key, edge[0], edge[1])

    def relax(self, u, v, w) -> None:
        if (
            self.graph[v]["property"]["distance"]
            > self.graph[u]["property"]["distance"] + w
        ):
            self.graph[v]["property"]["distance"] = (
                self.graph[u]["property"]["distance"] + w
            )
            self.graph[v]["property"]["parent"] = u


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of edge: "))
    for i in range(edges):
        u, v, w = map(int, input("Enter vertex, adjacent and weight: ").split(" "))
        g.addEdge(u, v, w)

    source = int(input("Enter Source: "))
    g.dijkstra(source)
    print("\nPrinting distance and parent: ")
    for key, val in g.graph.items():
        print(key, ":", val)


""" 
input 
3
1 2 10
1 3 20
2 3 5

6
1 2 10
1 3 20
2 3 40
3 4 10
5 4 5
3 5 2
1
"""
