#shortest path,bellman-ford
import sys
input=sys.stdin.readline
tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    edges=[]
    INF=float('inf')
    dist=[INF]*(n+1) #dist==0번 노드에서 다른 노드로 향하는 최단경로
    dist[0]=0 #가상 0번노드
    # 가상간선
    for i in range(1,n+1):
        edges.append((0,i,0))
    # 간선정보(양방향)
    for _ in range(m):
        s,e,t=map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    # 웜홀정보(단방향)
    for _ in range(w):
        sw,ew,tw=map(int,input().split())
        edges.append((sw,ew,-tw))
    
    for _ in range(n):
        for start,end,weight in edges:
            if dist[start]!=INF:
                dist[end]=min(dist[end],dist[start]+weight)
    
    cycle=False
    for start,end,weight in edges:
        if dist[start]+weight<dist[end]:
            cycle=True
            break

    print('YES' if cycle else 'NO')