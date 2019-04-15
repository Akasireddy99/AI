def iterative_dfs(graph,start,path=[]):
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
            path=path+[v]
            q=graph[v]+q
        return path
graph={'0':set(['1','2','3']),'1':set(['0','2']),'2':set(['0','4']),'3':set(['0']),'4':set(['2'])}
print(iterative_dfs(graph,'0'))