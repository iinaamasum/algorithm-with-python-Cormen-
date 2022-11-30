class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.time = 0

    def addEdge(self, u: int, v: int) -> None:
        if u in self.graph:
            self.graph[u]["adjacent"].append(v)
        else:
            self.graph[u] = {
                "property": {
                    "color": "white",
                    "discover_time": -1,
                    "finishing_time": -1,
                    "parent": None,
                },
                "adjacent": [v],
            }

        if v not in self.graph:
            self.graph[v] = {
                "property": {
                    "color": "white",
                    "discover_time": -1,
                    "finishing_time": -1,
                    "parent": None,
                },
                "adjacent": [],
            }

    # dfs function
    def dfs(self) -> None:
        for key in self.graph.keys():
            if self.graph[key]["property"]["color"] == "white":
                self.dfsVisit(key)

    # dfs visit function
    def dfsVisit(self, u) -> None:
        self.time += 1
        self.graph[u]["property"]["discover_time"] = self.time
        self.graph[u]["property"]["color"] = "gray"

        for v in self.graph[u]["adjacent"]:
            if self.graph[v]["property"]["color"] == "white":
                self.graph[v]["property"]["parent"] = u
                self.dfsVisit(v)

        self.time += 1
        self.graph[u]["property"]["finishing_time"] = self.time
        self.graph[u]["property"]["color"] = "black"

    # topology sort
    def topologySort(self) -> None:
        sorted_data = {}
        for key, val in self.graph.items():
            sorted_data[self.graph[key]["property"]["finishing_time"]] = key

        for i in reversed(sorted(sorted_data.keys())):
            print(sorted_data[i], end=",")
        print()


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of edges: "))
    for i in range(edges):
        u, v = map(int, input("Enter Edge: ").split(" "))
        g.addEdge(u, v)

    g.dfs()
    for key, val in g.graph.items():
        print(key, "->", val)
    print("\n\n")
    print("Topology Sort: ", end="")
    g.topologySort()

""" 
input
6
1 2
1 3
2 3
3 4
5 4
3 5

6
5 2
5 0
4 0
4 1
2 3
3 1
"""
