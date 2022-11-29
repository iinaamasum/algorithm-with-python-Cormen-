import sys
from queue import PriorityQueue
from heapq import heappush, heappop


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def insertHeap(self, val):
        heappush(self.heap, val)

    def extractMin(self):
        return heappop(self.heap)

    def parent(self, pos):
        return pos // 2

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )


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
        Q = MinHeap()

        for key, _ in self.graph.items():
            Q.insertHeap(key)

        while True:
            try:
                u = Q.extractMin()
            except:
                return
            S.append(u)

            for key, val in self.graph.items():
                for edge in val["adjacent"]:
                    is_relax = self.relax(key, edge[0], edge[1])
                    if is_relax:
                        Q.decreaseKey(
                            edge[0], self.graph[edge[0]]["property"]["distance"]
                        )

    def relax(self, u, v, w) -> None:
        if (
            self.graph[v]["property"]["distance"]
            > self.graph[u]["property"]["distance"] + w
        ):
            self.graph[v]["property"]["distance"] = (
                self.graph[u]["property"]["distance"] + w
            )
            self.graph[v]["property"]["parent"] = u
            return True

        else:
            return False


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of edge: "))
    for i in range(edges):
        u, v, w = map(int, input("Enter vertex, adjacent and weight: ").split(" "))
        g.addEdge(u, v, w)

    source = int(input("Enter Source: "))
    print(g.graph)
    g.dijkstra(source)


""" 
input 
3
1 2 10
1 3 20
2 3 5
"""
