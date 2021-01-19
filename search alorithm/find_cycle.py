graph = [
    [1,5],
    [2,0],
    [3,1],
    [6,4,2],
    [5,3],
    [0,4],
    [],
]

visited = [False]*len(graph)

list_history = set()

def dfs(visited,graph,node,start):
    visited[node] = True

    for neighbour in graph[node]:

        if visited[neighbour] == False:
            dfs(visited, graph, neighbour,node)
            list_history.add(neighbour)
        else:
            if neighbour in list_history:
                print("find",list_history,visited,neighbour)








dfs(visited,graph,1,2)


# set()
# {1}
# {0, 1}
# {0, 1, 5}
# {0, 1, 5}
# {0, 1, 4, 5}
# {0, 1, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5, 6}
# {0, 1, 2, 3, 4, 5, 6}
# {0, 1, 2, 3, 4, 5, 6}

