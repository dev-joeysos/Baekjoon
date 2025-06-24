#tag:graph,dfs
import sys
sys.setrecursionlimit(10**5)

input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    parent,child,weight=map(int,input().split())
    graph[parent].append((child,weight))
    graph[child].append((parent,weight))

def dfs(node,prev,dist):
    farthest_node=node
    max_dist=dist
    for next_node, weight in graph[node]:
        if next_node==prev:
            continue
        cand_node,cand_dist=dfs(next_node,node,dist+weight)
        if cand_dist>max_dist:
            max_dist=cand_dist
            farthest_node=cand_node
    return farthest_node, max_dist

start_node=1
fn1,_=dfs(start_node,-1,0)#가장 먼 노드를 찾는다.
fn2,answer=dfs(fn1,-1,0)#가장 먼 노드에서 가장 먼 노드를 찾는다==지름
print(answer)