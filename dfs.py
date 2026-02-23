'''Depth First Search uses STACK AND RECURSION'''
from collections import defaultdict
    def dfs(graph, start, visited, path):
        path.append(start)
        visited[start] = True
        for neighbour in graph[start]:
            if not visited[neighbour]:   # check if neighbour is not visited
                dfs(graph, neighbour, visited, path)   # recursive call
        return path

graph = defaultdict(list)
n, e = map(int, input().split())   # number of nodes and edges
for i in range(e):
    u, v = input().split()         # take edge input
    graph[u].append(v)             # add edge u -> v
    graph[v].append(u)             # add edge v -> u (if undirected)

start = 'A'
visited = defaultdict(bool)
path = []                          # initialize path list
traversedpath = dfs(graph, start, visited, path)
print(traversedpath)
