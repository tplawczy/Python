#the_map = np.zeros((N, N), dtype=int)

 #   for i in range(0, N):
  #      for j in range(0, i):
   #         if random.randint(0, 10) > p_zero:
    #            the_map[i][j] = random.randint(1, N)
     #           the_map[j][i] = the_map[i][j]

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys
import json
import numpy as np
sptSet = []

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print(
        "Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

            # A utility function to find the vertex with

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for count in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

    # Driver program
#the_map = np.zeros((10, 10), dtype=int)


g = Graph(99)
with open("network", "rb") as f:
    g.graph = json.load(f)

print(g.graph)


#g.graph= the_map
 #          [4, 0, 8, 0, 0, 0, 0, 11, 0],
  #         [0, 8, 0, 7, 0, 4, 0, 0, 2],
   #        [0, 0, 7, 0, 9, 14, 0, 0, 0],
    #       [0, 0, 0, 9, 0, 10, 0, 0, 0],
     #      [0, 0, 4, 14, 10, 0, 2, 0, 0],
      #     [0, 0, 0, 0, 0, 2, 0, 1, 6],
       #    [8, 11, 0, 0, 0, 0, 1, 0, 7],
        #   [0, 0, 2, 0, 0, 0, 6, 7, 0]
         #  ];

g.dijkstra(0);

# This code is contributed by Divyanshu Mehta