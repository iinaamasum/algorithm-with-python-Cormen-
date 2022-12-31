time = 0


class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.result = []

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
        self.result.append(u)

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

    print("\nDFS: ", end=" ")
    print(g.result)


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

""" 
Enter the number of edge: 6
Enter edge: 1 2
Enter edge: 1 3
Enter edge: 2 5
Enter edge: 2 4
Enter edge: 5 6
Enter edge: 4 7
1 :  {'property': {'color': 'black', 'discovery_time': 1, 'finishing_time': 14, 'parent': None}, 'adjacent': [2, 3]}
2 :  {'property': {'color': 'black', 'discovery_time': 2, 'finishing_time': 11, 'parent': 1}, 'adjacent': [5, 4]}
3 :  {'property': {'color': 'black', 'discovery_time': 12, 'finishing_time': 13, 'parent': 1}, 'adjacent': []}
5 :  {'property': {'color': 'black', 'discovery_time': 3, 'finishing_time': 6, 'parent': 2}, 'adjacent': [6]}
4 :  {'property': {'color': 'black', 'discovery_time': 7, 'finishing_time': 10, 'parent': 2}, 'adjacent': [7]}
6 :  {'property': {'color': 'black', 'discovery_time': 4, 'finishing_time': 5, 'parent': 5}, 'adjacent': []}
7 :  {'property': {'color': 'black', 'discovery_time': 8, 'finishing_time': 9, 'parent': 4}, 'adjacent': []}

DFS:  [1, 2, 5, 6, 4, 7, 3]
"""
