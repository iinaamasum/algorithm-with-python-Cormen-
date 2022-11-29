time = 0


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, u: int, v: int) -> None:

        if u in self.graph:
            self.graph[u]["adjacent"].append(v)
        else:
            self.graph[u] = {}
            self.graph[u]["property"] = {
                "color": "white",
                "discovery_time": -1,
                "finishing_time": -1,
                "parent": None,
            }
            self.graph[u]["adjacent"] = [v]
        if not v in self.graph:
            self.graph[v] = {}
            self.graph[v]["property"] = {
                "color": "white",
                "discovery_time": -1,
                "finishing_time": -1,
                "parent": None,
            }
            self.graph[v]["adjacent"] = []

    def dfs(self) -> None:
        for vertex in self.graph.keys():
            # print("keys: ", vertex)
            if self.graph[vertex]["property"]["color"] == "white":
                self.dfsVisit(vertex)

    def dfsVisit(self, u) -> None:
        global time
        time += 1
        # print(self.graph[u]["property"]["color"])
        self.graph[u]["property"]["color"] = "gray"
        self.graph[u]["property"]["discovery_time"] = time

        # calling all adjacent of u
        for v in self.graph[u]["adjacent"]:
            if self.graph[v]["property"]["color"] == "white":
                self.graph[v]["property"]["parent"] = u
                self.dfsVisit(v)

        time += 1
        self.graph[u]["property"]["finishing_time"] = time
        self.graph[u]["property"]["color"] = "black"


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of edge: "))
    for i in range(edges):
        u, v = map(int, input("Enter edge: ").split(" "))
        g.addEdge(u, v)

    g.dfs()
    for key, val in g.graph.items():
        print(key, ": ", val)


""" 
input 
3
1 2
1 3
2 3


6
1 2
1 3
2 3
3 4
5 4
3 5
"""
