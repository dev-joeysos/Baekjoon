# 백트래킹으로 중복순열 출력하기
# 단, 중복되는 중복순열은 출력하지 않는다.
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()

def dfs(start,path):
    if len(path)==m:
        print(*path)
        return 
    
    prev=-1
    for i in range(start,n):
        if prev==numbers[i]:
            continue
        dfs(i,path+[numbers[i]]) #numbers가 정렬됐기 때문에, 비내림차순으로 순열을 선택함.
        prev=numbers[i]
    
dfs(0,[])