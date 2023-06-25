from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Create graph using adjacency list representation
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # Define DFS function
        def DFS(current):
            # Check if the current vertex is the destination
            if current == destination:
                return True

            visited.add(current)
            # Explore neighboring vertices
            for neighbor in graph[current]:
                print(neighbor)
                if neighbor not in visited:
                    if DFS(neighbor):
                        return True

            return False

        # Iterate over all vertices and perform DFS starting from the source
        for vertex in range(n):
            if vertex not in visited and vertex == source:
                if DFS(vertex):
                    return True

        return False
