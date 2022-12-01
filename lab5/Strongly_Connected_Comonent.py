class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.tGraph = {}
        self.time = 0
        self.stack = []
        self.scc = []

    def addEdge(self, u: int, v: int) -> None:
        if u in self.graph:
            self.graph[u]["adjacent"].append(v)
        else:
            self.graph[u] = {
                "property": {
                    "color": "white",
                    "dis_time": -1,
                    "fin_time": -1,
                    "parent": None,
                },
                "adjacent": [v],
            }
        if v not in self.graph:
            self.graph[v] = {
                "property": {
                    "color": "white",
                    "dis_time": -1,
                    "fin_time": -1,
                    "parent": None,
                },
                "adjacent": [],
            }

    def dfs(self) -> None:
        for u in self.graph.keys():
            if self.graph[u]["property"]["color"] == "white":
                self.dfsVisit(self.graph, u)

    def dfsVisit(self, G, u: int) -> None:
        self.time += 1
        G[u]["property"]["color"] = "gray"
        G[u]["property"]["dis_time"] = self.time

        for v in G[u]["adjacent"]:
            if G[v]["property"]["color"] == "white":
                G[v]["property"]["parent"] = u
                self.dfsVisit(G, v)

        self.time += 1
        G[u]["property"]["color"] = "black"
        G[u]["property"]["fin_time"] = self.time

        # stack push element after finished
        self.stack.append(u)

    def stronglyConnectedComponent(self) -> None:
        self.stack = []
        self.transposeGraph()
        for u in self.tGraph.keys():
            if self.tGraph[u]["property"]["color"] == "white":
                self.dfsVisit(self.tGraph, u)
                self.scc.append(self.stack)
                self.stack = []

    def transposeGraph(self) -> None:
        for u in self.graph.keys():
            if u not in self.tGraph:
                self.tGraph[u] = {
                    "property": {
                        "color": "white",
                        "dis_time": -1,
                        "fin_time": -1,
                        "parent": None,
                    },
                    "adjacent": [],
                }
            for v in self.graph[u]["adjacent"]:
                if v not in self.tGraph:
                    self.tGraph[v] = {
                        "property": {
                            "color": "white",
                            "dis_time": -1,
                            "fin_time": -1,
                            "parent": None,
                        },
                        "adjacent": [u],
                    }
                else:
                    self.tGraph[v]["adjacent"].append(u)


if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter Edges: "))
    for i in range(edges):
        u, v = map(int, input("Enter Edge: ").split(" "))
        g.addEdge(u, v)
    # print(g.graph)
    g.dfs()
    g.stronglyConnectedComponent()
    print("\nTranspose Graph:")
    for key, val in g.tGraph.items():
        print(key, ":", val)

    print("\nSCC: ", end="")
    print(g.scc)


""" 
input 
10
0 1
1 2
2 0
2 3
3 4
4 5
4 7
5 6
6 4
6 7
"""
