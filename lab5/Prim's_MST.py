from sys import maxsize
from heapq import heappop, heappush


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {
                "property": {"color": "white"},
                "adjacent": [[v, w]],
            }
        else:
            self.graph[u]["adjacent"].append([v, w])

        if v not in self.graph:
            self.graph[v] = {
                "property": {"color": "white"},
                "adjacent": [[u, w]],
            }
        else:
            self.graph[v]["adjacent"].append([u, w])

    def primsMST(self, s):
        heap = []
        mst_sum = 0
        heappush(heap, (0, [s, -1]))
        mst = {}

        while heap:
            w, u = heappop(heap)
            if self.graph[u[0]]["property"]["color"] == "white":
                mst_sum += w
                self.graph[u[0]]["property"]["color"] = "gray"
                if u[1] != -1:
                    mst[u[1], u[0]] = w

                for v in self.graph[u[0]]["adjacent"]:
                    if self.graph[v[0]]["property"]["color"] == "white":
                        heappush(heap, (v[1], [v[0], u[0]]))

        print("\nMST Sum =", mst_sum)
        print("MST: ")
        print("edge\tweight")
        for key, val in mst.items():
            print(key, ":", val)


if __name__ == "__main__":
    g = Graph()
    weighted_edges = int(input("Enter the number of weighted edges: "))
    for i in range(weighted_edges):
        u, v, w = map(int, input("Enter edges with weight: ").split(" "))
        g.addEdge(u, v, w)
    g.primsMST(1)
    # print(g.graph)

""" 
input 
3
1 2 10
1 3 20
2 3 5

9
5 1 4
5 4 7
1 4 1
4 3 5
4 2 8
1 2 2
2 3 3
3 6 8
2 6 7
"""
