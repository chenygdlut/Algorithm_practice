def dijkstra(G,origin,target):
    N=len(G)
    dis=[float('inf') for _ in range(N)]
    visited=[0 for _ in range(N)]
    for i in range(N):
        if G[origin][i]>=0:
            dis[i]=G[origin][i]
    dis[origin]=0
    for i in range(N-1):
        distance=float('inf')
        cur=-1
        for j in range(N):
            if visited[j]==0 and dis[j]<distance:
                distance=dis[j]
                cur=j
        if cur==-1:
            continue
        visited[cur]=1
        for j in range(N):
            if visited[j]==0 and G[cur][j]!=-1 and G[cur][j]+dis[cur]<dis[j]:
                dis[j]=G[cur][j]+dis[cur]
    print(dis)
    return dis[target]

if __name__=='__main__':
    G=[
         [-1, -1, 10, -1, 30, 100],
         [-1, -1, 5, -1, -1, -1],
         [-1, -1, -1, 50, -1, -1],
         [-1, -1, -1, -1, -1, 10],
         [-1, -1, -1, 20, -1, 60],
         [-1, -1, -1, -1, -1, -1],
         ]
        
    
    print(dijkstra(G,0,5))