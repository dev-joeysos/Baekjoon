#permutation
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
visited=[False]*n

def dfs(path):
    if len(path)==m:#종료조건
        print(*path)
        return
    
    prev=-1
    for i in range(n):
        if not visited[i] and numbers[i]!=prev:
            visited[i]=True
            dfs(path+[numbers[i]])
            visited[i]=False
            prev=numbers[i] # 같은 depth에서 사용된 숫자를 기억
    
dfs([])