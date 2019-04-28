graph1 = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','I'],
    'D' : ['B','F'],
    'E' : ['B','G'],
    'F' : ['D','H'],
    'G' : ['E'],
    'H' : ['F'],
    'I' : ['C','J'],
    'J' : ['I']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)