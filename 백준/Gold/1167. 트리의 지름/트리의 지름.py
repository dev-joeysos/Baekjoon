#dfs
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
v=int(input())

graph=[[] for _ in range(v+1)]
for _ in range(v):
    line=list(map(int,input().split()))
    current_node=line[0]
    for i in range(1,len(line)-1,2):
        graph[current_node].append((line[i],line[i+1]))

def dfs(node,prev,dist):
    farthest_node=node
    max_dist=dist
    for next_node,weight in graph[node]:
        if next_node==prev:
            continue
        cand_node,cand_dist=dfs(next_node,node,dist+weight)
        if cand_dist>max_dist:
            max_dist=cand_dist
            farthest_node=cand_node
    return farthest_node,max_dist

f1,m1=dfs(1,-1,0)
f2,m2=dfs(f1,-1,0)
print(m2)