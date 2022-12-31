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
            self.graph[u]["property"] = {
                "parent": None,
                "distance": sys.maxsize,
            }
            self.graph[u]["adjacent"] = [[v, w]]

        if v not in self.graph:
            self.graph[v] = {}
            self.graph[v]["property"] = {
                "parent": None,
                "distance": sys.maxsize,
            }
            self.graph[v]["adjacent"] = []

    def dijkstra(self, s: int) -> None:
        self.graph[s]["property"]["distance"] = 0

        # taking result set
        S = set()
        Q = []

        for key in self.graph.keys():
            heappush(Q, key)

        while Q:
            u = heappop(Q)
            S = S.union({u})

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
3 5 2
5 4 5
1
"""

""" 
Enter the number of edge: 6
Enter vertex, adjacent and weight: 1 2 10
Enter vertex, adjacent and weight: 1 3 20
Enter vertex, adjacent and weight: 2 3 40
Enter vertex, adjacent and weight: 3 4 10
Enter vertex, adjacent and weight: 5 4 5
Enter vertex, adjacent and weight: 3 5 2
Enter Source: 1

Printing distance and parent: 
1 : {'property': {'parent': None, 'distance': 0}, 'adjacent': [[2, 10], [3, 20]]}
2 : {'property': {'parent': 1, 'distance': 10}, 'adjacent': [[3, 40]]}
3 : {'property': {'parent': 1, 'distance': 20}, 'adjacent': [[4, 10], [5, 2]]}
4 : {'property': {'parent': 5, 'distance': 27}, 'adjacent': []}
5 : {'property': {'parent': 3, 'distance': 22}, 'adjacent': [[4, 5]]}
"""
