def dijksta(start,n,w):
    INF = 10 ** 10
    dist = [INF] * n
    dist[start] = 0
    used = [False] * n
    min_dist = 0
    min_vertex = start
    while min_dist < INF:
        i = min_vertex
        used[i] = True
        for j in range(n):
            if dist[i] + w[i][j] < dist[j]:
                dist[j] = dist[i] + w[i][j]


        min_dist = INF
        for j in range(n):
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j
    print(dist)



marix = [
    [0,5,5],
    [5,0,0],
    [5,0,0]
]

dijksta(0,len(marix),marix)
