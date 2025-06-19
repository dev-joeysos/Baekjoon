
import sys
input=sys.stdin.readline
n=int(input())
lines=[list(map(int,input().split())) for _ in range(n)]

dp_max=[[0]*3 for _ in range(2)]
dp_min=[[0]*3 for _ in range(2)]

for i in range(n):
    v1,v2,v3=lines[i]
    if n==1:
        print(max(v1,v2,v3), min(v1,v2,v3))
        sys.exit()
    #첫번째 줄 초기화
    if i==0:
        dp_max[0][0],dp_max[0][1],dp_max[0][2]=v1,v2,v3
        dp_min[0][0],dp_min[0][1],dp_min[0][2]=v1,v2,v3
        continue
    #dp_max[1]은 이전 줄의 최댓값(dp_max[0])+현재줄
    #최댓값을 비교할 때, 리스트가 한 줄이면 최댓값을 구하고 저장하면서, 다음 최댓값을 구하는데 영향을 주게 됨
    dp_max[1][0]=v1+max(dp_max[0][0],dp_max[0][1])
    dp_max[1][1]=v2+max(dp_max[0][0],dp_max[0][1],dp_max[0][2])
    dp_max[1][2]=v3+max(dp_max[0][1],dp_max[0][2])
    
    dp_min[1][0]=v1+min(dp_min[0][0],dp_min[0][1])
    dp_min[1][1]=v2+min(dp_min[0][0],dp_min[0][1],dp_min[0][2])
    dp_min[1][2]=v3+min(dp_min[0][1],dp_min[0][2])
    
    #dp_max[0]에는 계산할 때 필요한 값을 저장
    #dp_max[1]에는 계산한 후의 결과를 저장
    dp_max[0][:]=dp_max[1][:]
    dp_min[0][:]=dp_min[1][:]
    
print(max(dp_max[0]),min(dp_min[0]))