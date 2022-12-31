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

        print("\nMST: ")
        print("edge\tweight")
        for key, val in mst.items():
            print(key, " : ", val)
        print("-" * 15)
        print("MST Sum =", mst_sum)


if __name__ == "__main__":
    g = Graph()
    weighted_edges = int(input("Enter the number of weighted edges: "))
    for i in range(weighted_edges):
        u, v, w = map(int, input("Enter edges with weight: ").split(" "))
        g.addEdge(u, v, w)
    source = int(input("Enter the source: "))
    g.primsMST(source)

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

""" 
Enter the number of weighted edges: 9
Enter edges with weight: 5 1 4
Enter edges with weight: 5 4 7
Enter edges with weight: 1 4 1
Enter edges with weight: 4 3 5
Enter edges with weight: 4 2 8
Enter edges with weight: 1 2 2
Enter edges with weight: 2 3 3
Enter edges with weight: 3 6 8
Enter edges with weight: 2 6 7
Enter the source: 1

MST: 
edge    weight
(1, 4)  :  1
(1, 2)  :  2
(2, 3)  :  3
(1, 5)  :  4
(2, 6)  :  7
---------------
MST Sum = 17
"""
