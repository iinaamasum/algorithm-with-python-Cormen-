class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.time = 0
        self.stack = []

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
        # for topological sort
        self.stack.append(u)

    # topology sort
    def topologySort(self) -> None:
        while self.stack:
            print(self.stack.pop(), end=" ")
        print()


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of edges: "))
    for i in range(edges):
        u, v = map(int, input("Enter Edge: ").split(" "))
        g.addEdge(u, v)

    g.dfs()
    print("\nTopology Sort: ", end="")
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

""" 
Enter the number of edges: 6
Enter Edge: 5 2
Enter Edge: 5 0
Enter Edge: 4 0
Enter Edge: 4 1
Enter Edge: 2 3
Enter Edge: 3 1

Topology Sort: 4 5 0 2 3 1 
"""
