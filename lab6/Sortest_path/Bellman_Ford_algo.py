import sys


# class Attribute:
#     def __init__(self) -> None:
#         self.parent = None
#         self.distance = 0


class Graph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices
        self.graph = [
            [
                {"weight": 0, "parent": None, "distance": sys.maxsize}
                for _ in range(vertices)
            ]
            for _ in range(vertices)
        ]

    def graph_input(self, graph_weight):
        for i in range(self.V):
            for j in range(self.V):
                self.graph[i][j]["weight"] = graph_weight[i][j]

    def init_single_source(self, s):
        # distance and parent already infinity and null while initialization
        s["distance"] = 0

    def relax(u, v, w):
        if v["distance"] > u["distance"] + w:
            v["distance"] = u["distance"] + w
            v["parent"] = u

    def bellman_ford_algo(self, source):
        self.init_single_source(source)

        for i in range(self.V - 1):
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph[i][j]["weight"] != 0:
                        self.relax()


if __name__ == "__main__":
    g = Graph(5)
    graph_weight = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    g.graph_input(graph_weight)
    print(g.graph)


""" 
        input
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0
"""
