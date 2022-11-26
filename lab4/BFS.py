from sys import maxsize
from queue import Queue
import pandas as pd


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, u: int, v: int) -> None:
        attribute = {
            "color": "white",
            "distance": maxsize,
            "parent": None,
        }

        if u in self.graph:
            self.graph[u]["adjacent"].append(v)
        else:
            self.graph[u] = {}
            self.graph[u]["property"] = attribute
            self.graph[u]["adjacent"] = [v]
        if not v in self.graph:
            self.graph[v] = {}
            self.graph[v]["property"] = attribute
            self.graph[v]["adjacent"] = []

    def bfs(self, s: int) -> None:
        # discovering source
        self.graph[s]["property"] = {"color": "gray", "distance": 0}
        # taking a queue
        Q = Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            print("getting Q: ", u)

            # checking all adjacent
            for v in self.graph[u]["adjacent"]:
                if self.graph[v]["property"]["color"] == "white":
                    self.graph[v]["property"] = {
                        "color": "gray",
                        "distance": self.graph[u]["property"]["distance"] + 1,
                        "parent": u,
                    }

                    Q.put(v)

            # finishing u
            self.graph[u]["property"]["color"] = "black"


if __name__ == "__main__":
    g = Graph()
    vertices = int(input("Number of vertices: "))
    for i in range(vertices):
        u, v = map(int, input("Vertex & Adjacent: ").split(" "))
        g.addEdge(u, v)

    g.bfs(1)
    df = pd.DataFrame(g.graph)
    print(df)


""" 
input
3
1 2
1 3
2 3
"""
